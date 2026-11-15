import json
import websocket

# 1. Substitua pelos seus dados reais obtidos na Deriv
APP_ID = pat_b3dbc429d8426329763158033227eb4a15352e78181bb57c2cd9558ef223fa8c
API_TOKEN = 34XJdt9B7m6B1ncYBQy04  # O seu token gerado nas definições da conta

URL = f"wss://ws.derivws.com/websockets/v3?app_id={APP_ID}"


def on_message(ws, message):
  data = json.loads(message)
  print("Resposta recebida da Deriv:", json.dumps(data, indent=2))

  # Verifica se a autorização foi concluída com sucesso
  if data.get("msg_type") == "authorize":
    if "error" in data:
      print("Erro na autorização:", data["error"]["message"])
    else:
      print("Autorizado com sucesso! Conexão estabelecida e ativa.")
      # Aqui pode adicionar a lógica de subscrição de ticks ou ordens de negociação


def on_error(ws, error):
  print(f"Erro na ligação WebSocket: {error}")


def on_close(ws, close_status_code, close_msg):
  print("Conexão com a Deriv foi fechada.")


def on_open(ws):
  print("Conectado ao servidor da Deriv! A enviar autorização...")
  auth_request = {"authorize": API_TOKEN}
  ws.send(json.dumps(auth_request))


if __name__ == "__main__":
  ws = websocket.WebSocketApp(
      URL,
      on_open=on_open,
      on_message=on_message,
      on_error=on_error,
      on_close=on_close,
  )
  ws.run_forever()
