from flask import jsonify, request
from app.logging.redis_logger import log_event
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

        log_event('success operation', 'pow', f'base={data.base}, exp={data.exp}', str(result))

        return jsonify(ResultResponse(result=result).model_dump()), 200

    except ValidationError as ve:
        input_data = request.get_json()
        log_event('validation error', 'pow', str(input_data), error=str(ve))
        return jsonify({"error": ve.errors()}), 422

    except Exception as e:
        input_data = request.get_json()
        log_event('server_error', 'pow', str(input_data), error=str(e))
        return jsonify({"error": str(e)}), 400
    
def calculate_fib():
    try:
        data = FibRequest.model_validate(request.get_json())
        result = fibonacci(data.n)

        op = Operation(operation="fib", input_data=f'n={data.n}', result=str(result))
        db.session.add(op)
        db.session.commit()

        log_event('success operation', 'fib', f'n={data.n}', str(result))

        return jsonify(ResultResponse(result=result).model_dump()), 200
    
    except ValidationError as ve:
        input_data = request.get_json()
        log_event('validation error', 'fib', str(input_data), error=str(ve))
        return jsonify({'error' : ve.errors()}), 422
    
    except Exception as e:
        input_data = request.get_json()
        log_event('server_error', 'fib', str(input_data), error=str(e))
        return jsonify({'error' : str(e)}), 400
    
def calculate_fact():
    try:
        date = FactRequest.model_validate(request.get_json())
        result = factorial(date.n)

        op = Operation(operation='fact', input_data=f'n={date.n}', result=str(result))

        db.session.add(op)
        db.session.commit()

        log_event('success operation', 'fact', f'n={date.n}', str(result))

        return jsonify(ResultResponse(result=result).model_dump()), 200
    except ValidationError as ve:
        input_data = request.get_json()
        log_event('validation error', 'fact', str(input_data), error=str(ve))
        return jsonify({'error' : ve.errors()}), 422
    except Exception as e:
        input_data = request.get_json()
        log_event('server_error', 'fact', str(input_data), error=str(e))
        return jsonify({'error' : str(e)}) , 400

    
    
