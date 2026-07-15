// noscript.js
const express = require('express');
const multer = require('multer');
const ffmpeg = require('fluent-ffmpeg');
const path = require('path');
const fs = require('fs');

const router = express.Router();

// Configure temporary file upload storage
const upload = multer({ 
  dest: 'uploads/',
  limits: { fileSize: 10 * 1024 * 1024 } // Limit to 10MB
});

/**
 * POST /convert-noscript
 * Standard multi-part form submission fallback
 */
router.post('/convert-noscript', upload.single('gifFile'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('<h1>Error: No GIF file uploaded.</h1><a href="/">Go Back</a>');
  }

  const inputPath = req.file.path;
  const outputName = `${Date.now()}-converted.mp4`;
  const outputPath = path.join(__dirname, 'uploads', outputName);

  // Convert GIF to MP4 using native system ffmpeg
  ffmpeg(inputPath)
    .outputOptions([
      '-pix_fmt yuv420p',      // Ensures high compatibility with web players
      '-c:v libx264',          // Use standard H.264 video codec
      '-movflags +faststart',  // Allows progressive loading
    ])
    .toFormat('mp4')
    .on('end', () => {
      // Stream the file back for download, then clean up temp files
      res.download(outputPath, 'converted-video.mp4', (err) => {
        // Cleanup uploads
        try {
          fs.unlinkSync(inputPath);
          fs.unlinkSync(outputPath);
        } catch (cleanupError) {
          console.error('Error cleaning up temp files:', cleanupError);
        }
      });
    })
    .on('error', (err) => {
      console.error('FFmpeg Conversion Error:', err);
      res.status(500).send('<h1>Failed to convert GIF to Video.</h1><a href="/">Try Again</a>');
      // Cleanup the uploaded input file
      try { fs.unlinkSync(inputPath); } catch (e) {}
    })
    .save(outputPath);
});

module.exports = router;
