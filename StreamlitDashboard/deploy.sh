#!/bin/bash
# ============================================================
# Deploy Streamlit Dashboard to Google Cloud Run
# ============================================================
# Usage: ./deploy.sh [PROJECT_ID] [REGION]
# Example: ./deploy.sh my-gcp-project asia-south1
# ============================================================

set -e

PROJECT_ID="${1:-$(gcloud config get-value project 2>/dev/null)}"
REGION="${2:-asia-south1}"
SERVICE_NAME="ml-dashboard"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

if [ -z "$PROJECT_ID" ]; then
    echo "❌ No GCP project ID provided."
    echo "Usage: ./deploy.sh <PROJECT_ID> [REGION]"
    echo "   or: gcloud config set project <PROJECT_ID> && ./deploy.sh"
    exit 1
fi

echo "============================================"
echo "  Deploying to Google Cloud Run"
echo "  Project:  $PROJECT_ID"
echo "  Region:   $REGION"
echo "  Service:  $SERVICE_NAME"
echo "============================================"

# Step 1: Enable required APIs
echo ""
echo "🔧 Step 1: Enabling APIs..."
gcloud services enable run.googleapis.com containerregistry.googleapis.com cloudbuild.googleapis.com \
    --project="$PROJECT_ID" --quiet

# Step 2: Build + push using Cloud Build (no local Docker needed!)
echo ""
echo "🐳 Step 2: Building container via Cloud Build..."
gcloud builds submit \
    --tag "$IMAGE_NAME" \
    --project="$PROJECT_ID" \
    --quiet

# Step 3: Deploy to Cloud Run
echo ""
echo "🚀 Step 3: Deploying to Cloud Run..."
gcloud run deploy "$SERVICE_NAME" \
    --image "$IMAGE_NAME" \
    --platform managed \
    --region "$REGION" \
    --allow-unauthenticated \
    --memory 1Gi \
    --cpu 1 \
    --timeout 300 \
    --max-instances 2 \
    --project="$PROJECT_ID" \
    --quiet

# Step 4: Get the URL
echo ""
echo "============================================"
URL=$(gcloud run services describe "$SERVICE_NAME" \
    --platform managed \
    --region "$REGION" \
    --project="$PROJECT_ID" \
    --format="value(status.url)")
echo "  ✅ DEPLOYED SUCCESSFULLY!"
echo "  🌐 URL: $URL"
echo "============================================"
