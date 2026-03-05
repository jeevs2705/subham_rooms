# Quick Guide: Add Your Room Image

## Steps to Add the Room Image:

### Option 1: Manual Copy (Easiest)
1. Save your room image to your computer
2. Make 3 copies of the image
3. Rename them to:
   - `room-small4.jpg`
   - `room-small2.jpg`
   - `room-big8.jpg`
4. Copy all 3 files to: `C:\Users\gayat\OneDrive\Desktop\room-booking-app\static\images\`
5. Refresh your website - the images will appear!

### Option 2: Using Windows Explorer
1. Open File Explorer
2. Navigate to: `C:\Users\gayat\OneDrive\Desktop\room-booking-app\static\images\`
3. Paste your room image here 3 times
4. Rename each copy:
   - First copy → `room-small4.jpg`
   - Second copy → `room-small2.jpg`
   - Third copy → `room-big8.jpg`

### Option 3: Using Command (if you have the image saved)
If your image is saved as `room.jpg` in Downloads folder:
```bash
cd static/images
copy "C:\Users\gayat\Downloads\room.jpg" room-small4.jpg
copy "C:\Users\gayat\Downloads\room.jpg" room-small2.jpg
copy "C:\Users\gayat\Downloads\room.jpg" room-big8.jpg
```

## Where the Images Will Appear:
- **Home Page**: In the "Our Rooms" section (3 room cards)
- **Room Details Pages**: When users click on each room
- **Booking Page**: As reference for customers

## Image Tips:
- The image you shared looks perfect for a hotel room!
- You can use the same image for all rooms initially
- Later, you can replace with specific photos for each room type
- Recommended size: 800x600 pixels
- Keep file size under 2MB

## Current Image Locations:
```
static/images/
├── room-small4.jpg  ← Add here (Small Room - 4 People)
├── room-small2.jpg  ← Add here (Mini Room - 2 People)
├── room-big8.jpg    ← Add here (Big Room - 8 People)
└── restroom.jpg     ← Optional: Add restroom photo
```

## After Adding Images:
1. Refresh your browser (Ctrl + F5)
2. Visit http://127.0.0.1:5000/
3. You should see your room images instead of the 🛏️ emoji!

## Need More Images?
You can also add detail images for room detail pages:
- room-small4-2.jpg, room-small4-3.jpg (additional angles)
- room-small2-2.jpg, room-small2-3.jpg
- room-big8-2.jpg, room-big8-3.jpg
