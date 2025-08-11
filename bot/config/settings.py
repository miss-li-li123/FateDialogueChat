import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_community.chat_models import ChatOpenAI

# 加载环境变量
env_path = Path(__file__).parent.parent / "deepseek.env"
load_dotenv(env_path)

class DeepSeekConfig(BaseSettings):
    """DeepSeek API配置模型"""
    model: str = "deepseek-chat"
    openai_api_key: str = os.getenv("DEEPSEEK_API_KEY", "")
    openai_api_base: str = os.getenv("DEEPSEEK_API_BASE", "")
    temperature: float = 0.0
    streaming: bool = True
    
    # 使用新的配置方式
    model_config = SettingsConfigDict(
        env_prefix="DEEPSEEK_",
        case_sensitive=False
    )
    
    def create_chat_model(self) -> ChatOpenAI:
        """创建并返回配置好的ChatOpenAI实例"""
        return ChatOpenAI(
            model=self.model,
            openai_api_key=self.openai_api_key,
            openai_api_base=self.openai_api_base,
            temperature=self.temperature,
            streaming=self.streaming
        )

class AppConfig(BaseSettings):
    """全局应用配置"""
    deepseek: DeepSeekConfig = DeepSeekConfig()
    serpapi_api_key: str = os.getenv("SERPAPI_API_KEY", "")
    
    def setup_environment(self):
        """设置必要的环境变量"""
        os.environ["OPENAI_API_KEY"] = self.deepseek.openai_api_key
        os.environ["OPENAI_API_BASE"] = self.deepseek.openai_api_base
        os.environ["SERPAPI_API_KEY"] = self.serpapi_api_key
    
    def get_chat_model(self) -> ChatOpenAI:
        """获取配置好的ChatOpenAI实例"""
        return self.deepseek.create_chat_model()

# 单例配置实例
app_config = AppConfig()
app_config.setup_environment()