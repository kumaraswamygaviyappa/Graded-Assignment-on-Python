# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:41:43 2024

@author: Kumaraswamy Gaviyappa
"""

import re
import psutil
import time
import configparser
import json
import os
from flask import Flask, jsonify

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config_data = {}
    
    try:
        config.read(file_path)
        
        for section in config.sections():
            config_data[section] = {}
            for key, value in config.items(section):
                config_data[section][key] = value

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except configparser.Error as e:
        print(f"Error: {e}")
    
    return config_data

def save_to_json(data, output_file):
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    try:
        with open('config_data.json', 'r') as json_file:
            config_data = json.load(json_file)
        return jsonify(config_data)
    except Exception as e:
        return jsonify({'error': str(e)})

def monitor_cpu_usage(threshold):
    print("Monitoring CPU usage...")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU usage Alert @{threshold}%: {cpu_usage}%")
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return False
    
    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for digits
    if not re.search(r'\d', password):
        return False
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def Q1():
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Your password is strong!")
    else:
        print("Your password is weak. Please choose a stronger password that meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains both uppercase and lowercase letters")
        print("- Contains at least one digit (0-9)")
        print("- Contains at least one special character (e.g., !, @, #, $, %)")

if __name__ == "__main__":
    print("Q1 : Check the strength of the password!")
    Q1()
    
    print("Q1 : Check the strength of the password!")
    Q1()
    
    print("Q2 : Monitor the health of the CPU!")
    threshold = 80  # You can set the threshold to any percentage you prefer
    monitor_cpu_usage(threshold)
    
    print("Q3 : automating configuration management!")
    config_data = read_config_file('config.ini')    
    if config_data:
        save_to_json(config_data, 'config_data.json')    
    app.run(host='0.0.0.0', port=5000)
