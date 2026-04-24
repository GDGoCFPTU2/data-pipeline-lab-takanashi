from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================


class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp).
    Các trường này sẽ được sử dụng để lưu trữ và truy vấn tài liệu trong hệ thống.
    """

    # Khai báo các trường ở đây...
    document_id: str = Field(..., description="Unique identifier for the document")
    source_type: str = Field(
        ..., description="Type of the source (e.g., 'pdf', 'web', 'email')"
    )
    author: str = Field(..., description="Author of the document")
    category: str = Field(
        ...,
        description="Category of the document (e.g., 'news', 'research', 'personal')",
    )
    content: str = Field(..., description="Content of the document")
    timestamp: str = Field(
        ..., description="Timestamp of when the document was created or ingested"
    )
