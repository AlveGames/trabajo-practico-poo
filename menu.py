class Menu:
    """Reusable class to display and handle console menus."""

    def __init__(self, title, options):
        """
        :param title: Menu title string
        :param options: dict {number: (label, callable)}
        """
        self.title = title
        self.options = options

    def display(self):
        """Print the menu options."""
        print("\n" + "=" * 50)
        print(f"  {self.title}")
        print("=" * 50)
        for key, (label, _) in self.options.items():
            print(f"  {key}. {label}")
        print("  0. Exit")
        print("=" * 50)

    def run(self):
        """Main loop: show menu and execute selected option."""
        while True:
            self.display()
            choice = input("  Select an option: ").strip()

            if choice == "0":
                print("\n  Goodbye!\n")
                break
            elif choice in self.options:
                label, action = self.options[choice]
                print(f"\n  Running: {label}\n")
                action()
            else:
                print("\n  Invalid option, please try again.")
