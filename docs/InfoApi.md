# harmony_connect_client.InfoApi

All URIs are relative to *https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_info**](InfoApi.md#get_all_info) | **GET** / | API Info


# **get_all_info**
> AllInfo get_all_info()

API Info

Request general information about the Connect API such as the version and available endpoints.

### Example

* Api Key Authentication (AppId): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppId
configuration.api_key['app_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.InfoApi(harmony_connect_client.ApiClient(configuration))

try:
    # API Info
    api_response = api_instance.get_all_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_all_info: %s\n" % e)
```


* Api Key Authentication (AppKey): 
```python
from __future__ import print_function
import time
import harmony_connect_client
from harmony_connect_client.rest import ApiException
from pprint import pprint
configuration = harmony_connect_client.Configuration()
# Configure API key authorization: AppKey
configuration.api_key['app_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# create an instance of the API class
api_instance = harmony_connect_client.InfoApi(harmony_connect_client.ApiClient(configuration))

try:
    # API Info
    api_response = api_instance.get_all_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->get_all_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllInfo**](AllInfo.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

