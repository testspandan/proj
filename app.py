from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/find_subdomains', methods=['POST'])
def find_subdomains():
    try:
        target_domain = request.json['domain']
        # Using subprocess to execute the subfinder command
        result = subprocess.run(['subfinder', '-d', target_domain], capture_output=True, text=True)
        subdomains = result.stdout.splitlines()
        return jsonify({'subdomains': subdomains})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
