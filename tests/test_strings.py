from toolkit_py.strings import camel_case, kebab_case, slugify, snake_case


def test_slugify_basic() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_snake_case() -> None:
    assert snake_case("Hello Python Toolkit") == "hello_python_toolkit"


def test_kebab_case() -> None:
    assert kebab_case("Hello Python Toolkit") == "hello-python-toolkit"


def test_camel_case() -> None:
    assert camel_case("hello python toolkit") == "helloPythonToolkit"
