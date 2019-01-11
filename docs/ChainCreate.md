# ChainCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ids** | **list[str]** | Tags that can be used to identify your chain. You can search for records that contain a particular external_id using Connect. You must send External IDs in Base64 format. | 
**content** | **str** | This is the data that will make up the first entry in your new chain. It is customary to use this space to describe the entries that are to follow in the chain. You must send the content field in Base64 format. | 
**callback_url** | **str** | The URL where you would like to receive the callback from Connect. If this is not specified, callbacks will not activate. | [optional] 
**callback_stages** | **list[str]** | The stages that you would like to trigger a callback from Connect. This list can include any or all of the three stages: &#x60;replicated&#x60;, &#x60;factom&#x60;, and &#x60;anchored&#x60;. If callbacks are activated and this field is not sent, it will default to &#x60;factom&#x60; and &#x60;anchored&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


