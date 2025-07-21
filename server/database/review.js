// Load environment variables from .env file (use dynamic import workaround for ES modules)
import dotenv from 'dotenv';
dotenv.config();

import { Schema as _Schema, model } from 'mongoose';
const Schema = _Schema;

// Optionally access env variables here
const apiKey = process.env.NLU_API_KEY;
const apiUrl = process.env.NLU_API_URL;
// console.log(apiKey, apiUrl); // Optional debug

// Define the Review schema
const ReviewSchema = new Schema({
  id: {
    type: Number,
    required: true,
  },
  name: {
    type: String,
    required: true
  },
  dealership: {
    type: Number,
    required: true,
  },
  review: {
    type: String,
    required: true
  },
  purchase: {
    type: Boolean,
    required: true
  },
  purchase_date: {
    type: String,
    required: true
  },
  car_make: {
    type: String,
    required: true
  },
  car_model: {
    type: String,
    required: true
  },
  car_year: {
    type: Number,
    required: true
  },
  sentiment: {
    type: String,        // ✅ Watson NLU sentiment result
    required: false      // Optional
  }
});

// Export the Review model
export default model('Review', ReviewSchema);
