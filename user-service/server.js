const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

mongoose.connect("mongodb://localhost:27017/blog", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const UserSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
});

const User = mongoose.model("User", UserSchema);

// რეგისტრაციის API
app.post("/register", async (req, res) => {
  const { username, email, password } = req.body;
  const user = new User({ username, email, password });
  await user.save();
  res.send({ message: "User registered" });
});

// ავტორიზაციის API
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email, password });
  if (user) {
    res.send({ token: "fake-jwt-token" });
  } else {
    res.status(401).send({ message: "Invalid credentials" });
  }
});

app.listen(3000, () => {
  console.log("User service running on port 3000");
});
