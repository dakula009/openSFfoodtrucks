import requests
from Tools import QueryMaker


def get_data(url):
    """
    This function gets the data from the API.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('\nSomething went wrong when getting the data..')
        return None


def print_results(data):
    """
    This function prints the formatted data in the console
    """
    if data == []:
        print('\nNo data to display')
    else:
        print('SF Food trucks available now:\n')
        for item in data:
            name = item['applicant']
            address = item['location']
            print(f'NAME:{name}             ADDRESS:{address}')


keep_going = True
page_num = 0


while keep_going:
    """
    This while loop lets user proceed to see all pages avaiable, or quit the program
    """

    url = QueryMaker(page_num).make_query()
    data = get_data(url)
    if not data:
        # if there was previous a page shown, then indeed no more to show
        if page_num > 0:
            print('\nNo more food trucks to show. See you next time!')
        # nothing has been displayed yet, meaning there is no data in the beginning
        else:
            print('\nNo food truck available at this moment. See you next time!')
        break
    else:
        print_results(data)
        print(f'\n======Page {page_num + 1}======')

        # if the data obtained still has 10 records, then let user proceed
        if len(data) == 10:
            user_input = input("\nWanna see more? (y/n): ")

            if user_input in ['Y', 'Yes', 'y', 'yes']:
                page_num += 1
            else:
                print('\nSee you next time!')

                break
        # if the data obtained is less than 10 records, terminate the program
        else:
            print('\nNo more food trucks to show. See you next time!')
            break

