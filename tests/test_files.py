from pathlib import Path

from toolkit_py.files import ensure_dir, list_files, read_text, write_text


def test_write_and_read_text(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    write_text(file_path, "hello")
    assert read_text(file_path) == "hello"


def test_ensure_dir(tmp_path: Path) -> None:
    directory = ensure_dir(tmp_path / "nested" / "path")
    assert directory.exists()
    assert directory.is_dir()


def test_list_files(tmp_path: Path) -> None:
    write_text(tmp_path / "a.txt", "a")
    write_text(tmp_path / "nested" / "b.txt", "b")
    names = sorted(path.name for path in list_files(tmp_path, "*.txt"))
    assert names == ["a.txt", "b.txt"]
