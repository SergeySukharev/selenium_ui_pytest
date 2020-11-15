from OpencartSearch import Search


def test_opencart_search(browser, base_url):
    opencart_main_page = Search(browser, base_url)
    opencart_main_page.go_to_site()
    opencart_main_page.enter_word("MacBook")
    opencart_main_page.click_on_the_search_button()
    elements = opencart_main_page.search_results()
    for elem in elements:
        assert "MacBook" in elem.text
