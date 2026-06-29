# pip install cx_freeze
import cx_Freeze
executaveis = [
    cx_Freeze.Executable(
        script="main.py",
        icon="assets/icone.ico",
        target_name="CaféDaFirma.exe"
    ) ]
cx_Freeze.setup(
    name = "Café Da Firma",
    options={
        "build.exe":{
            "include_files":["assets","recursos"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi