# EntryData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_hash** | **str** | The SHA256 Hash of this entry. | 
**chain** | [**EntryListChain**](EntryListChain.md) |  | 
**created_at** | **str** | The time when this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: &#x60;YYYY-MM-DDThh:mm:ss.ssssssZ&#x60; | 
**external_ids** | **list[str]** | Tags that can be used to identify your entry. You can search for records that contain a particular external_id using Connect. External IDs are returned in Base64. | 
**content** | **str** | This is the data that is stored by the entry. Content will be sent in Base64 format. | 
**stage** | **str** | The level of immutability that this entry has reached. | 
**dblock** | [**EntryDataDblock**](EntryDataDblock.md) |  | [optional] 
**eblock** | [**EntryDataEblock**](EntryDataEblock.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


