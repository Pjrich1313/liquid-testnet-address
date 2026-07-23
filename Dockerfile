# Dockerfile for RPC Auth Generator
FROM python:3.12-slim

WORKDIR /app

# Copy the script
COPY generate_rpcauth.py .

# Make it executable
RUN chmod +x generate_rpcauth.py

# Default command
ENTRYPOINT ["python3", "generate_rpcauth.py"]
CMD ["--help"]