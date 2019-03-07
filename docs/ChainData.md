# ChainData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | This is the unique identifier created for each chain. | 
**content** | **str** | This is the data that was stored in the first entry of this chain. | 
**external_ids** | **list[str]** | Tags that have been used to identify this entry. | 
**stage** | **str** | The immutability stage that this chain has reached. | 
**entries** | [**ChainDataEntries**](ChainDataEntries.md) |  | 
**eblock** | [**ChainDataEblock**](ChainDataEblock.md) |  | [optional] 
**dblock** | [**ChainDataDblock**](ChainDataDblock.md) |  | [optional] 
**created_at** | **str** | The time at which this chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: &#x60;YYYY-MM-DDThh:mm:ss.ssssssZ&#x60; This will be null if the chain is not at least at the &#x60;factom&#x60; immutability stage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


