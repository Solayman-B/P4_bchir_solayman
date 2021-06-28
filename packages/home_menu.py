

class HomeMenuView:
	def __init__(self, menu):
		self.menu = menu

	def _display_menu(self):
		for key, entry in self.menu.items():
			print(f"{key}: {entry.option}\n")

	def get_user_choice(self):
		# afficher le menu
		self._display_menu()

		# demander un choix à l'utilisateur
		while True:
			choise = input(">> ")

		# valider le choix
		if choice in self.menu:
			# retourner le choix
			return self.menu[choice]
