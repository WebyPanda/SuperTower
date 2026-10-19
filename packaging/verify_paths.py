import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / "src"
RESOURCE_CALLS = {
    "pygame.font.Font",
    "pygame.image.load",
    "pygame.mixer.Sound",
    "pygame.mixer.music.load",
    "open",
}


def resource_pattern(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return "" if node.id == "asset_root" else "*"
    if isinstance(node, ast.JoinedStr):
        parts = [
            value.value if isinstance(value, ast.Constant) else "*"
            for value in node.values
        ]
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = resource_pattern(node.left)
        right = resource_pattern(node.right)
        if left is not None and right is not None:
            return left + right
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        left = resource_pattern(node.left)
        right = resource_pattern(node.right)
        if left is not None and right is not None:
            return str(Path(left) / right)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id in {"str", "asset_path", "Path"} and node.args:
            return resource_pattern(node.args[0])
    if isinstance(node, ast.Subscript):
        return "*"
    return None


def main() -> None:
    failures = []
    checked = 0

    for script in sorted(SOURCE_ROOT.rglob("*.py")):
        tree = ast.parse(script.read_text(encoding="utf-8-sig"), filename=str(script))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            call_name = ast.unparse(node.func)
            if call_name not in RESOURCE_CALLS or not node.args:
                continue

            pattern = resource_pattern(node.args[0])
            if pattern is None:
                failures.append(
                    f"{script.relative_to(ROOT)}:{node.lineno}: "
                    f"cannot determine {call_name} path ({ast.unparse(node.args[0])})"
                )
                continue

            pattern = pattern.replace("\\", "/")
            if not pattern.startswith("assets/"):
                failures.append(
                    f"{script.relative_to(ROOT)}:{node.lineno}: "
                    f"resource path is not rooted in assets/ ({pattern})"
                )
                continue

            checked += 1
            if not any(ROOT.glob(pattern)):
                failures.append(
                    f"{script.relative_to(ROOT)}:{node.lineno}: "
                    f"{call_name} path does not match an asset ({pattern})"
                )

    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Verified {checked} resource paths in all source scripts.")


if __name__ == "__main__":
    main()
