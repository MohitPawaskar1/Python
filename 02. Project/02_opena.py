from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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")

command = '''
[21:54, 4/2/2025] PU0003_Mohit_Pawaskar: Bhand to meine bhi code strach se hi kiya tha��
[21:55, 4/2/2025] Charlotte: Arre pagal wo libraries class sub
[21:56, 4/2/2025] Charlotte: Tuj sochna bhand tera ye abhi 5 min mai hua
[21:56, 4/2/2025] Charlotte: Usko ek pointer badhane ko 6 ghante lage
[22:00, 4/2/2025] PU0003_Mohit_Pawaskar: ohh
[22:03, 4/2/2025] Charlotte: Wojna
[22:03, 4/2/2025] Charlotte: Tu bhi hhi kr
[22:03, 4/2/2025] Charlotte: Wo bola ki usne ye ek project kiya usmai uske itne concepts clr hue na
[22:03, 4/2/2025] Charlotte: Teko bhi acha rhega
[22:04, 4/2/2025] Charlotte: Koi easy model se strt krr aur scratch se lik taaki smja
[22:04, 4/2/2025] Charlotte: Smjega*
[22:07, 4/2/2025] PU0003_Mohit_Pawaskar: Haa krta krta
[22:08, 4/2/2025] PU0003_Mohit_Pawaskar: But ye pythob tha ya ml?
'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Mohit who speaks hindi as well as english. He is from India and is a coder. "
    "You analyze chat history and respond like Mohit"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)