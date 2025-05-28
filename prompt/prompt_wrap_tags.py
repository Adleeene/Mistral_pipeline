from typing import Literal


def prompt_wrap_tags(
    user_prompt: str,
    system_prompt: str = "",
    model_type: Literal["mistral", "llama"] = "mistral",
):
    if model_type == "mistral":
        prompt = "<s>[INST] " + user_prompt + "[/INST]"
    elif model_type == "llama":
        prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|> 
        {system_prompt}
        
        You are a helpful assistant<|eot_id|>

        <|start_header_id|>user<|end_header_id|>
        {user_prompt}<|eot_id|>

        <|start_header_id|>assistant<|end_header_id|>"""
    else:
        raise Exception(f"Invalid argument type for model type: {model_type}")
    return prompt
