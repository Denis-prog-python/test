import requests
from typing import Optional


def get_random_cat_image() -> Optional[str]:
    """
    Запрашивает случайное изображение кошки с TheCatAPI.

    Returns:
        str: URL изображения кошки, если запрос успешен.
        None: Если запрос неудачный (например, статус код не 200 или произошла ошибка).
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Генерирует исключение при статусе 4xx/5xx
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0].get("url")
        return None
    except (requests.RequestException, ValueError):
        return None


if __name__ == "__main__":
    cat_url = get_random_cat_image()
    if cat_url:
        print(f"Ссылка на случайного кота: {cat_url}")
    else:
        print("Не удалось получить изображение кота.")