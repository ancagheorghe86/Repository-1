class example_Json:
    file_path_txt = "C:\\Users\\WDG\\PycharmProjects\\pythonProject\\pythonProject5\\requirments.txt"

    def citeste_fisier_text(self):
        with open(file=self.file_path_txt, mode="r") as fisier:
            # pt. Json
            # Json.load(fisier)
            return fisier.readlines()

    def scriere_fisier(self):
        with open(self.file_path_txt, "a") as fisier:
            fisier.writelines("teste")


e = example_Json()
e.citeste_fisier_text()
print(e.citeste_fisier_text())
e.scriere_fisier()
print(e.citeste_fisier_text())


