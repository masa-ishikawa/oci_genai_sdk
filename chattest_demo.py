import oci
import time
import json
from oci.auth.signers import InstancePrincipalsSecurityTokenSigner
from oci.generative_ai_inference.generative_ai_inference_client import GenerativeAiInferenceClient
from oci.generative_ai_inference.models import (
    ChatDetails,
    OnDemandServingMode,
    CohereChatRequest,
    CohereTool,
    CohereParameterDefinition,
    CohereToolCall,
    CohereToolResult
)

compartment_id = "(my_compartment_id)"
endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
# config = oci.config.from_file(
#     file_location='~/.oci/config', profile_name="CHICAGO")
# config = oci.config.from_file(
#     file_location='~/.oci/config')
# print(config)
signer = InstancePrincipalsSecurityTokenSigner()
generative_ai_inference_client = GenerativeAiInferenceClient(
    config={}, signer=signer, service_endpoint=endpoint)
# generative_ai_inference_client = GenerativeAiInferenceClient(
#     config=config, service_endpoint=endpoint)

previous_chat_system_message = oci.generative_ai_inference.models.CohereSystemMessage(
    role="SYSTEM", message="あなたはクラシック音楽よりもラップ、hiphopを愛する音楽家です。")
previous_chat_user_message = oci.generative_ai_inference.models.CohereUserMessage(
    role="USER", message="仕事がはかどる音楽は何？")
previous_chat_chatbot_message = oci.generative_ai_inference.models.CohereChatBotMessage(
    role="CHATBOT", message="ラップやヒップホップがおすすめです！クラシック音楽よりも刺激的で、仕事中に聞いても眠くならないからです。特に、アップテンポなビートとポジティブな歌詞が仕事のモチベーションを上げてくれます。")

chat_request = CohereChatRequest(
    message="その理由を500文字程度で回答して",
    max_tokens=1000,
    is_stream=True,
    is_echo = True,
)
chat_request.chat_history = [previous_chat_system_message,
                             previous_chat_user_message, previous_chat_chatbot_message]
# chat_request.chat_history = []
# chat_request.documents = []
response = generative_ai_inference_client.chat(
    chat_details=ChatDetails(
        compartment_id=compartment_id,
        serving_mode=OnDemandServingMode(
            model_id="cohere.command-r-plus"
        ),
        chat_request=chat_request
    )
)

start_time = time.perf_counter()
first_token_time = None
print("**************************Streaming Chat Response**************************")
chat_history = []
chatbot_message = ""
citations = []
finish_reason = ""
prompt = ""
for event in response.data.events():
    res = json.loads(event.data)
    if first_token_time is None:
        first_token_time = time.perf_counter()
    if 'finishReason' in res.keys():
        finish_reason = res['finishReason']
        if 'chatHistory' in res:
            chat_history = res['chatHistory']
        if 'text' in res:
            chatbot_message = res['text']
        if 'citations' in res:
            citations = res['citations']
        if 'prompt' in res:
            prompt = res['prompt']
        break
    if 'text' in res:
        print(res['text'], end="", flush=True)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
# print("**************************Chat History*************************************")
# for history in chat_history:
#     print(f"Role: {history['role']}, Message: {history['message']}\n")
# print("**************************Chatbot Message**********************************")
# print(f"text:\n{chatbot_message}\n")
# print("**************************Citations****************************************")
# for i, citation in enumerate(citations, start=1):
#     print(f"Citation {i}:")
#     print(f"  Document IDs: {citation['documentIds']}")
#     print(f"  Start: {citation['start']}")
#     print(f"  End: {citation['end']}")
#     print(f"  Text: {citation['text']}")
#     print()
# print("**************************Finish Reason************************************")
# print(f"finish_reason:{finish_reason}\n")
# print("**************************Prompt*******************************************")
# print(f"prompt:{prompt}\n")
# print("**************************Inference Time***********************************")
# if first_token_time is not None:
#     first_token_elapsed = first_token_time - start_time
#     print(f"time to first token: {first_token_elapsed:.2f} sec")
# print(f"total inference time: {elapsed_time:.2f} sec")
