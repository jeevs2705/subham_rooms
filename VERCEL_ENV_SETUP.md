# How to Add GOOGLE_CREDENTIALS to Vercel

## Step-by-Step Instructions

### 1. After Your First Deployment on Vercel

Once your app is deployed, you'll see the project dashboard.

### 2. Go to Project Settings

- Click on "Settings" tab (top menu)
- Click on "Environment Variables" in the left sidebar

### 3. Add GOOGLE_CREDENTIALS Variable

Click "Add New" and fill in:

**Key (Name):**
```
GOOGLE_CREDENTIALS
```

**Value:**
Copy the content from your `credentials.json` file, but format it as a SINGLE LINE with no spaces or line breaks.

**How to format it:**
1. Open your `credentials.json` file
2. Copy ALL the content
3. Remove all line breaks and extra spaces
4. It should look like: `{"type":"service_account","project_id":"...","private_key":"...","client_email":"..."}`
5. Paste this single line into Vercel

**Important:** The entire JSON must be on ONE line!

**Environment:** Select "Production, Preview, and Development"

Click "Save"

### 4. Add Other Environment Variables

Repeat the process for these:

**Variable 2:**
- Key: `GOOGLE_SHEET_NAME`
- Value: `Room bookings`

**Variable 3:**
- Key: `ADMIN_USERNAME`
- Value: `vignesh`

**Variable 4:**
- Key: `ADMIN_PASSWORD`
- Value: `vignesh`

### 5. Redeploy

After adding all variables:
- Go to "Deployments" tab
- Click the "..." menu on the latest deployment
- Click "Redeploy"
- Wait 2-3 minutes

### Done!

Your app will now have access to Google Sheets!

## Important Notes:

- The credentials are stored securely by Vercel
- Never share these credentials publicly
- The JSON must be on ONE LINE (no line breaks) - that's why it looks compressed above
- Make sure to copy the ENTIRE content including the curly braces { }

## Troubleshooting:

If Google Sheets doesn't work:
1. Make sure you copied the entire JSON (starts with { and ends with })
2. Check there are no extra spaces or line breaks
3. Verify the sheet name matches exactly: "Room bookings"
4. Confirm the service account email has access to your Google Sheet
