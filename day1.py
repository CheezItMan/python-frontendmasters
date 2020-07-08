import requests


def create_query(languages, min_stars=50000):
    query = f"stars>:{min_stars} "
    for language in languages:
        query += f"language:{language} "
    return {"q": query}


def repos_with_most_stars(languages, sort="stars", order="desc"):
    GH_API_REPO_SEARCH_URL = "https://api.github.com/search/repositories"
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GH_API_REPO_SEARCH_URL, params)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(
            f"An error occured.  Status code was: {status_code}")
    response_json = response.json()

    return response_json


if __name__ == "__main__":
    # main method

    languages = ["Python", "Javascript", "Ruby"]
    repos = repos_with_most_stars(languages)["items"]
    # print(repos)
    for repo in repos:
        language = repo["language"]
        stars = repo["stargazers_count"]
        name = repo["name"]
        url = repo["html_url"]
        print(f"--> {name} is a {language} repo with {stars} stars at {url}.")
