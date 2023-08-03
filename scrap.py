from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


def scrapper(search_result):
    data = []

    try:
        # 1. Rating
        rating_span = search_result.find('div', itemprop="reviewRating").find('span', itemprop='ratingValue')
        rating = rating_span.text.strip() if rating_span else None
        data.append(rating)

        # 2. Header
        header_h2 = search_result.find('div', class_="body").find('h2', class_='text_header')
        header = header_h2.text.strip() if header_h2 else None
        data.append(header)

        # 3. Customer Name, Country, Date
        customer_info_h3 = search_result.find('div', class_="body").find('h3', class_='text_sub_header userStatusWrapper')
        customer_name_span = customer_info_h3.find('span', itemprop='name')
        customer_name = customer_name_span.text.strip() if customer_name_span else None
        data.append(customer_name)

        # Country (Australia) is in parentheses, so we need to extract it using regex
        country_regex = r'\((.*?)\)'
        country_match = re.search(country_regex, customer_info_h3.text)
        country = country_match.group(1) if country_match else None
        data.append(country)

        date_published_time = customer_info_h3.find('time', itemprop='datePublished')
        date = date_published_time.text.strip() if date_published_time else None
        data.append(date)

        # 4. Is Verified
        review_body_div = search_result.find('div', class_='text_content')
        is_verified_em = review_body_div.find('em')
        is_verified = is_verified_em.text.strip() if is_verified_em else None
        data.append(is_verified)

        # 5. Review
        review = review_body_div.text.strip() if review_body_div else None
        data.append(review)

        # 6. Type of Traveller
        type_of_traveller_td = search_result.find('div', class_="body").find('td', class_='review-rating-header type_of_traveller')
        type_of_traveller = type_of_traveller_td.find_next('td', class_='review-value').text.strip() if type_of_traveller_td else None
        data.append(type_of_traveller)

        # 7. Seat Type
        seat_type_td = search_result.find('div', class_="body").find('td', class_='review-rating-header cabin_flown')
        seat_type = seat_type_td.find_next('td', class_='review-value').text.strip() if seat_type_td else None
        data.append(seat_type)

        # 8. Route
        route_td = search_result.find('div', class_="body").find('td', class_='review-rating-header route')
        route = route_td.find_next('td', class_='review-value').text.strip() if route_td else None
        data.append(route)

        # 9. Date Flown
        date_flown_td = search_result.find('div', class_="body").find('td', class_='review-rating-header date_flown')
        date_flown = date_flown_td.find_next('td', class_='review-value').text.strip() if date_flown_td else None
        data.append(date_flown)

        # 10. Seat Comfort
        seat_comfort_td = search_result.find('td', class_='review-rating-header seat_comfort')
        seat_comfort_span = seat_comfort_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if seat_comfort_td else None
        seat_comfort = max([int(span.text) for span in seat_comfort_span]) if seat_comfort_span else None
        data.append(seat_comfort)

        # 11. Cabin Staff Service
        cabin_staff_service_td = search_result.find('td', class_="review-rating-header cabin_staff_service")
        cabin_staff_service_span = cabin_staff_service_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if cabin_staff_service_td else None
        cabin_staff_service = max([int(span.text) for span in cabin_staff_service_span]) if cabin_staff_service_span else None
        data.append(cabin_staff_service)

        # 12. Food & Beverages
        food_and_beverages_td = search_result.find('td', class_="review-rating-header food_and_beverages")
        food_and_beverages_span = food_and_beverages_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if food_and_beverages_td else None
        food_and_beverages = max([int(span.text) for span in food_and_beverages_span]) if food_and_beverages_span else None
        data.append(food_and_beverages)

        # 13. Inflight Entertainment
        inflight_entertainment_td = search_result.find('td', class_="review-rating-header inflight_entertainment")
        inflight_entertainment_span = inflight_entertainment_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if inflight_entertainment_td else None
        inflight_entertainment = max([int(span.text) for span in inflight_entertainment_span]) if inflight_entertainment_span else None
        data.append(inflight_entertainment)

        # 14. Ground Service
        ground_service_td = search_result.find('td', class_="review-rating-header ground_service")
        ground_service_span = ground_service_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if ground_service_td else None
        ground_service = max([int(span.text) for span in ground_service_span]) if ground_service_span else None
        data.append(ground_service)

        # 15. Wifi & Connectivity
        wifi_and_connectivity_td = search_result.find('td', class_="review-rating-header wifi_and_connectivity")
        wifi_and_connectivity_span = wifi_and_connectivity_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if wifi_and_connectivity_td else None
        wifi_and_connectivity = max([int(span.text) for span in wifi_and_connectivity_span]) if wifi_and_connectivity_span else None
        data.append(wifi_and_connectivity)

        # 16. Value For Money
        value_for_money_td = search_result.find('td', class_="review-rating-header value_for_money")
        value_for_money_span = value_for_money_td.find_next('td', class_="review-rating-stars stars").find_all('span', class_='star fill') if value_for_money_td else None
        value_for_money = max([int(span.text) for span in value_for_money_span]) if value_for_money_span else None
        data.append(value_for_money)

        # 17. Recommended
        recommended_td = search_result.find('td', class_='review-rating-header recommended')
        recommended = recommended_td.find_next('td', class_='review-value rating-no').text.strip() if recommended_td else None
        data.append(recommended)

        # print(f'Successfully Scrapped Review of {customer_name}')

    except:
        pass

    return data


if __name__ == '__main__':

    final_data_list = []
    NULL = "None"

    # Scrapping data from website
    for i in range(1, 13):
        URL = f"https://www.airlinequality.com/airline-reviews/air-india/page/{i}/?sortby=post_date%3ADesc&pagesize=100"
        response = requests.get(URL)
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        search_results = soup.find_all("article", itemprop="review")

        for result in search_results:
            final_data_list.append(scrapper(result))

        # print(f"Successfully Scrapped Data From Page No. {i}")

    # Convert nested list to a DataFrame
    columns = ['rating', 'header', 'customer_name', 'country', 'date', 'is_verified', 'review', 'type_of_traveller',
               'seat_type', 'route', 'date_flown', 'seat_comfort', 'cabin_staff_service', 'food_and_beverages',
               'inflight_entertainment', 'ground_service', 'wifi_and_connectivity', 'value_for_money', 'recommended']
    df = pd.DataFrame(final_data_list, columns=columns)

    # Write DataFrame to CSV file
    df.to_csv('output_data.csv', index=False)

