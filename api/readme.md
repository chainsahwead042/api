# PDU Monitoring API - Cloud Run Deployment

## Deployment Instructions

1. Login to GCP
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID

2. Build Docker image
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/pdu-api

3. Deploy to Cloud Run
   gcloud run deploy pdu-api \
     --image gcr.io/YOUR_PROJECT_ID/pdu-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated

4. Access API
   Open the URL provided by Cloud Run, e.g.:
   https://pdu-api-xxxx.a.run.app/metrics

## Notes
- Replace the SNMP IP & community string in main.py with your actual PDU.
- For private LAN PDUs, you may need VPN or port forwarding.
- Cloud Run automatically scales for multiple users.
