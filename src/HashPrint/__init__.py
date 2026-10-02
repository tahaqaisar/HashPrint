# In the Name of God, the Most Compassionate, Most Merciful


from importlib.metadata import PackageNotFoundError, version, metadata

try:
    __version__ = version("pyhashprint")
    __project_name__ = metadata("pyhashprint").get("Name")
except PackageNotFoundError:
    __version__ = "1.0.0"
    __project_name__ = "pyhashprint"
