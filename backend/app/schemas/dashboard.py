from pydantic import BaseModel, Field

class MetricsIngestRequest(BaseModel):
    metric_name: str = Field(..., description="Name of the incoming metric")
    value: float = Field(..., description="Numerical value of the metric")
    source: str = Field("default_sensor", description="Source device or system identifier")

class MetricsResponse(BaseModel):
    status: str
    processed_metric: str
    transformed_value: float
    message: str