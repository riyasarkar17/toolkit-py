from toolkit_py import camel_case, list_files, slugify

print(slugify("Toolkit Py Example"))
print(camel_case("toolkit py example"))
print([str(path) for path in list_files(".", "*.py")][:5])
