import wikipedia
from bs4 import BeautifulSoup


def main():
    while True:
        # Get search term from user
        title = input("\nEnter page title: ").strip()

        # Exit if user enters blank input
        if not title:
            print("Thank you.")
            break

        try:
            # Try to get the page
            page = wikipedia.page(title)

            # Print the details
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            # Handle multiple possible pages
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])  # Show first 5 options to keep output manageable

        except wikipedia.PageError:
            # Handle page not found
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
