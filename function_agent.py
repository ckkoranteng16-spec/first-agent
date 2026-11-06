import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

genai.configure(api_key=api_key)

def functions(name,argument):
    {
        "alxValue":alxValue
        "bpeEncode":bpeEncode
        "cipher":cipher
        "decipher":decipher
        "gridWalker":gridWalker
        "isBalanced":isBalanced
        "scoreWord":scoreword
        "sortAscending":sortAscending
        "daysToDeadline":daysToDeadline
    }


def alxValue(text):
   asciisum = 0
   for char in text:
    asciisum+=ord(char)
  
    av=(asciisum//2)+1
   status = "ALX certified" if av % 2 == 0 else "Not ALX certified"
   return {
       "text": text,
       "ascii_sum": asciisum,
       "alx_value": av,
       "status": status,
   }


def bpeEncode(text, steps):
    from collections import Counter
    from string import ascii_uppercase

    if len(text) < 2:
        return text, {}

    alphabet = reversed(ascii_uppercase)   
    swap = {}                               

    for step in range(steps):
        if len(text) < 2:
            break

        pairs = [text[i:i+2] for i in range(len(text) - 1)]
        count = Counter(pairs)

        totalCount= max(count.values())
        #print(pairs,totalCount)
        if totalCount <= 1:
            break  

        
        firstPair = next(pair for pair in pairs if count[pair] == totalCount)


        token = next(alphabet)

     
        newText = []
        i = 0
        while i < len(text):
            if i < len(text) - 1 and text[i:i+2] == firstPair:
                newText.append(token)
                i += 2
            else:
                newText.append(text[i])
                i += 1
        text = "".join(newText)

        swap[token] = firstPair
    return text, swap



def cipher(message,steps):
    encrypted=[]
    for char in message:
        if char.isupper():
            codeNum=(((ord(char)-65)+steps)%26)+65
            char=chr(codeNum)
            encrypted.append(char)
        elif char.islower():
            codeNum=(((ord(char)-97)+steps)%26)+97
            char=chr(codeNum)
            encrypted.append(char)

        else:
            encrypted.append(char)
    return "".join(encrypted)



def decipher(message,steps):
    results = []
    for i in range(1,steps+1):
        deciphered=[]
    
        for char in message:
            if char.isupper():
                codeNum=(((ord(char)-65)-i)%26)+65
                deciphered.append(chr(codeNum))
                
            elif char.islower():
                codeNum=(((ord(char)-97)-i)%26)+97
                deciphered.append(chr(codeNum))
                
            else:
                deciphered.append(chr(256-ord(char)))
              
        results.append({"shift": i, "message": "".join(deciphered)})
    return results
    

def gridWalker(path):
    x0, y0 = (0, 0)
    coordinates={(x0,y0)}
    directions = { 'U': (0, 1),'D': (0, -1),'L': (-1, 0),'R': (1, 0) }
    distanceTracker=0
    for move in path:
        if move in directions:
            x1, y1 = directions[move]
            x0 += x1
            y0 += y1
            coordinates.add((x0, y0))
            dist=int(abs(x0)) + int(abs(y0))
            if dist>distanceTracker:
                distanceTracker=dist
    finpos = (x0, y0)
    manhattan_distance = abs(finpos[0]) + abs(finpos[1])
    uniquePosition=len(set(coordinates))
    return {
        "final_position": finpos,
        "manhattan_distance": manhattan_distance,
        "unique_positions": uniquePosition,
        "furthest_distance_travelled": distanceTracker,
    }
   

def isBalanced(text):
   stack=[]
   Brackets={']':'[' , '}':'{' , ')':'('}
   for char in text:
    if char in Brackets.values():
        stack.append(char)
    elif char in Brackets.keys():
        if not stack or stack[-1] != Brackets[char]:
            return False
        stack.pop()
   return len(stack)==0



def scoreword(word):
    word="".join([char for char in word if char.isalpha()]).lower()
    
    if len(word) <1:
        points=0
    elif len(set(word)) < len(word):
        points =len(word)//2
    else:
        points=len(word)
    return points
    
def sortAscending(text):
    characters = [i for i in text]
    arranged = []
    uniChar = []
    newString = []
    
    for char in characters:
        asciiNum = ord(char)
        uniChar.append(asciiNum)
    
    for num in uniChar:
        if not arranged:
            arranged.append(num)
        else:
            inserted = False
            for charPos in range(len(arranged)):
                if num > arranged[charPos]:
                    arranged.insert(charPos, num)
                    inserted = True
                    break
            if not inserted:
                arranged.append(num)
    
    for num in arranged:
        new = chr(num)
        newString.append(new)
    newString=''.join(newString)
    return newString


def daysToDeadline(submission_day):
    from datetime import datetime, date

    try:
        submission_day = submission_day.strip()

        try:
            deadline = datetime.strptime(submission_day, '%d/%m/%Y').date()
        except ValueError:
            deadline = datetime.strptime(submission_day.title(), '%d %B %Y').date()

        currentDate = date.today()
        numdays = deadline - currentDate

        if numdays.days < 0:
            return {"status": "passed", "days_remaining": numdays.days}

        weekslft = numdays.days // 7
        dayslft = numdays.days % 7

    except (ValueError, AttributeError):
        return {"error": 'Invalid input. Date format should be dd/mm/yyyy or "day Month year".'}
    else:
        return {
            "status": "upcoming",
            "weeks_remaining": weekslft,
            "days_remaining": dayslft,
            "total_days_remaining": numdays.days,
        }


model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools=[functions]
)

chat = model.start_chat(enable_automatic_function_calling=True)

def run(user_message):
    response=chat.send_message(user_message)
    return response.text

print("=== Full turn-by-turn trace ===")
for turn in chat.history:
    for part in turn.parts:
        if getattr(part, "function_call", None):
            print(turn.role, "-> CALLS TOOL:", part.function_call.name,
                  dict(part.function_call.args))
        elif getattr(part, "function_response", None):
            print(turn.role, "-> TOOL RETURNED:",
                  dict(part.function_response.response))
        elif getattr(part, "text", None):
            print(turn.role, "-> TEXT:", part.text)
