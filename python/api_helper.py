def check_endpoint_info(sent_data, expected_data):
    try:    
        for data in expected_data:
            if(sent_data.get(data) == None):
                return f'the {data} must be sent!'
    except TypeError:
        print('Invalid entry. (how could this happen?)')
    except:
        print('Something went wrong with endpoint info check.')
