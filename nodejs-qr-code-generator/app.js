const express = require("express");
const path = require("path");
const QRCode = require("qrcode");

const app = express();
const port = 3000;

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("index", { qrCode: null });
});

app.post("/generate", async (req, res) => {
  const url = req.body.url;
  const color = req.body.color || "#000000";
  const size = parseInt(req.body.size) || 10;
  const errorCorrection = req.body.errorCorrection || "L";

  try {
    const qrOptions = {
      errorCorrectionLevel: errorCorrection,
      type: "image/png",
      color: {
        dark: color,
        light: "#FFFFFF",
      },
      scale: size,
    };

    const qrCode = await QRCode.toDataURL(url, qrOptions);
    const qrSVG = await QRCode.toString(url, { ...qrOptions, type: "svg" });

    res.render("index", { qrCode, qrSVG });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error generating QR code");
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
