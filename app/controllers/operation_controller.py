from flask import jsonify, request
from app.services.operation_service import power, fibonacci, factorial
from app.models.operation import Operation
from app.db.db import db
from pydantic import ValidationError
from app.schemas.operation_schemas import (
    PowRequest,
    FibRequest,
    FactRequest,
    ResultResponse
)

def calculate_pow():
    try:
        data = PowRequest.model_validate(request.get_json())
        result = power(data.base, data.exp)
        op = Operation(operation="pow", input_data=f"base={data.base},exp={data.exp}", result=str(result))
        db.session.add(op)
        db.session.commit()
        return jsonify(ResultResponse(result=result).model_dump()), 200
    except ValidationError as ve:
        return jsonify({"error": ve.errors()}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
def calculate_fib():
    try:
        data = FibRequest.model_validate(request.get_json())
        result = fibonacci(data.n)
        op = Operation(operation="fib", input_data=f"n={data.n}", result=str(result))
        db.session.add(op); db.session.commit()
        return jsonify(ResultResponse(result=result).model_dump()), 200
    except ValidationError as ve:
        return jsonify({"error": ve.errors()}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def calculate_fact():
    try:
        data = FactRequest.model_validate(request.get_json())
        result = factorial(data.n)
        op = Operation(operation="fact", input_data=f"n={data.n}", result=str(result))
        db.session.add(op); db.session.commit()
        return jsonify(ResultResponse(result=result).model_dump()), 200
    except ValidationError as ve:
        return jsonify({"error": ve.errors()}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    
    
