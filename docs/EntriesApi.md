# harmony_connect_client.EntriesApi

All URIs are relative to *https://connect-shared-sandbox-2445582615332.production.gw.apicast.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entries_by_chain_id**](EntriesApi.md#get_entries_by_chain_id) | **GET** /chains/{chain_id}/entries | Get Chain&#39;s Entries
[**get_entry_by_hash**](EntriesApi.md#get_entry_by_hash) | **GET** /chains/{chain_id}/entries/{entry_hash} | Get Entry Info
[**get_first_entry**](EntriesApi.md#get_first_entry) | **GET** /chains/{chain_id}/entries/first | Get Chain&#39;s First Entry
[**get_last_entry**](EntriesApi.md#get_last_entry) | **GET** /chains/{chain_id}/entries/last | Get Chain&#39;s Last Entry
[**post_entries_search**](EntriesApi.md#post_entries_search) | **POST** /chains/{chain_id}/entries/search | Search Chain&#39;s Entries
[**post_entry_to_chain_id**](EntriesApi.md#post_entry_to_chain_id) | **POST** /chains/{chain_id}/entries | Create an Entry


# **get_entries_by_chain_id**
> EntryList get_entries_by_chain_id(chain_id, limit=limit, offset=offset, stages=stages)

Get Chain's Entries

List all entries contained on the specified chain.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The page you would like to request. The first page offset is Zero. (optional)
stages = 'stages_example' # str | The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. If you would like to search among multiple stages, send them in a comma separated string. For example: `'multi_az,factom'`. (optional)

try:
    # Get Chain's Entries
    api_response = api_instance.get_entries_by_chain_id(chain_id, limit=limit, offset=offset, stages=stages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entries_by_chain_id: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The page you would like to request. The first page offset is Zero. (optional)
stages = 'stages_example' # str | The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. If you would like to search among multiple stages, send them in a comma separated string. For example: `'multi_az,factom'`. (optional)

try:
    # Get Chain's Entries
    api_response = api_instance.get_entries_by_chain_id(chain_id, limit=limit, offset=offset, stages=stages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entries_by_chain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 
 **limit** | **int**| The number of items you would like back in each page. | [optional] 
 **offset** | **int**| The page you would like to request. The first page offset is Zero. | [optional] 
 **stages** | **str**| The immutability stages you want to restrict results to. You can choose any from &#x60;replicated&#x60;, &#x60;factom&#x60;, and &#x60;anchored&#x60;. If you would like to search among multiple stages, send them in a comma separated string. For example: &#x60;&#39;multi_az,factom&#39;&#x60;. | [optional] 

### Return type

[**EntryList**](EntryList.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entry_by_hash**
> Entry get_entry_by_hash(chain_id, entry_hash)

Get Entry Info

Returns information about a specific entry on Connect. The requested entry must be specified using the Chain ID and Entry Hash.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
entry_hash = db # str | The SHA256 hash of the entry.

try:
    # Get Entry Info
    api_response = api_instance.get_entry_by_hash(chain_id, entry_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry_by_hash: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
entry_hash = db # str | The SHA256 hash of the entry.

try:
    # Get Entry Info
    api_response = api_instance.get_entry_by_hash(chain_id, entry_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_entry_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 
 **entry_hash** | **str**| The SHA256 hash of the entry. | 

### Return type

[**Entry**](Entry.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_first_entry**
> Entry get_first_entry(chain_id)

Get Chain's First Entry

Retrieve the first entry that has been saved to this chain.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier

try:
    # Get Chain's First Entry
    api_response = api_instance.get_first_entry(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_first_entry: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier

try:
    # Get Chain's First Entry
    api_response = api_instance.get_first_entry(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_first_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 

### Return type

[**Entry**](Entry.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_entry**
> Entry get_last_entry(chain_id)

Get Chain's Last Entry

Retrieve the last entry that has been saved to this chain.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier

try:
    # Get Chain's Last Entry
    api_response = api_instance.get_last_entry(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_last_entry: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier

try:
    # Get Chain's Last Entry
    api_response = api_instance.get_last_entry(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->get_last_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 

### Return type

[**Entry**](Entry.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_entries_search**
> EntrySearchResponse post_entries_search(chain_id, search_body, limit=limit, offset=offset)

Search Chain's Entries

Find all of the entries within the specified chain that have the requested `external_ids`.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
search_body = harmony_connect_client.SearchBody() # SearchBody | 
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The page you would like to request. The first page offset is Zero. (optional)

try:
    # Search Chain's Entries
    api_response = api_instance.post_entries_search(chain_id, search_body, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->post_entries_search: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
search_body = harmony_connect_client.SearchBody() # SearchBody | 
limit = 15 # int | The number of items you would like back in each page. (optional)
offset = 2 # int | The page you would like to request. The first page offset is Zero. (optional)

try:
    # Search Chain's Entries
    api_response = api_instance.post_entries_search(chain_id, search_body, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->post_entries_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 
 **search_body** | [**SearchBody**](SearchBody.md)|  | 
 **limit** | **int**| The number of items you would like back in each page. | [optional] 
 **offset** | **int**| The page you would like to request. The first page offset is Zero. | [optional] 

### Return type

[**EntrySearchResponse**](EntrySearchResponse.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_entry_to_chain_id**
> EntryShort post_entry_to_chain_id(chain_id, entry_create)

Create an Entry

Create a new entry for the selected chain. Content and external id must be uploaded in Base64 format.

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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
entry_create = harmony_connect_client.EntryCreate() # EntryCreate | 

try:
    # Create an Entry
    api_response = api_instance.post_entry_to_chain_id(chain_id, entry_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->post_entry_to_chain_id: %s\n" % e)
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
api_instance = harmony_connect_client.EntriesApi(harmony_connect_client.ApiClient(configuration))
chain_id = 285904 # str | Chain identifier
entry_create = harmony_connect_client.EntryCreate() # EntryCreate | 

try:
    # Create an Entry
    api_response = api_instance.post_entry_to_chain_id(chain_id, entry_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntriesApi->post_entry_to_chain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Chain identifier | 
 **entry_create** | [**EntryCreate**](EntryCreate.md)|  | 

### Return type

[**EntryShort**](EntryShort.md)

### Authorization

[AppId](../README.md#AppId), [AppKey](../README.md#AppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

