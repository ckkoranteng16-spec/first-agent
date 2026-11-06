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
        "alxValue":alxValue,
        "bpeEncode":bpeEncode,
        "cipher":cipher,
        "decipher":decipher,
        "gridWalker":gridWalker,
        "isBalanced":isBalanced,
        "scoreWord":scoreword,
        "sortAscending":sortAscending,
        "daysToDeadline":daysToDeadline
    }


def alxValue(text):
    """Calculate the ALX value of a string.

    Args:
        text (str): Input text.

    Returns:
        dict: Original text, ASCII sum, ALX value and certification status.
    """
    asciisum = 0

    for char in text:
        asciisum += ord(char)

    # Calculate the ALX value, handling empty input safely.
    av = (asciisum // 2) + 1 if text else 0

    # Determine certification status.
    status = "ALX certified" if av % 2 == 0 else "Not ALX certified"

    return {
        "text": text,
        "ascii_sum": asciisum,
        "alx_value": av,
        "status": status,
    }


def bpeEncode(text, steps):
    """Encode text using a simplified Byte Pair Encoding approach.

    Args:
        text (str): Text to encode.
        steps (int): Maximum number of merging operations.

    Returns:
        tuple: Encoded text and a dictionary mapping tokens to pairs.
    """
    from collections import Counter
    from string import ascii_uppercase

    # Return early if there are not enough characters to form a pair.
    if len(text) < 2:
        return text, {}

    # Use uppercase letters in reverse order as replacement tokens.
    alphabet = reversed(ascii_uppercase)
    swap = {}

    for step in range(steps):
        if len(text) < 2:
            break

        # Identify all adjacent character pairs.
        pairs = [text[i:i+2] for i in range(len(text) - 1)]

        # Count the frequency of each pair.
        count = Counter(pairs)
        totalCount = max(count.values())

        # Stop when no pair occurs more than once.
        if totalCount <= 1:
            break

        # Select the most frequent pair.
        # The first occurrence breaks ties.
        firstPair = next(
            pair for pair in pairs if count[pair] == totalCount
        )

        # Assign a new token to the selected pair.
        token = next(alphabet)

        newText = []
        i = 0

        # Replace occurrences of the selected pair.
        while i < len(text):
            if i < len(text) - 1 and text[i:i+2] == firstPair:
                newText.append(token)
                i += 2
            else:
                newText.append(text[i])
                i += 1

        # Update the encoded text.
        text = "".join(newText)

        # Store the token and the pair it represents.
        swap[token] = firstPair

    return text, swap


def cipher(message, steps):
    """Encrypt a message using a Caesar-style letter shift.

    Args:
        message (str): Message to encrypt.
        steps (int): Number of positions to shift letters.

    Returns:
        str: Encrypted message.
    """
    encrypted = []

    for char in message:
        if char.isupper():
            # Shift uppercase letters and wrap around the alphabet.
            codeNum = (((ord(char) - 65) + steps) % 26) + 65
            char = chr(codeNum)
            encrypted.append(char)

        elif char.islower():
            # Shift lowercase letters and wrap around the alphabet.
            codeNum = (((ord(char) - 97) + steps) % 26) + 97
            char = chr(codeNum)
            encrypted.append(char)

        else:
            # Preserve spaces, numbers and punctuation.
            encrypted.append(char)

    return "".join(encrypted)


def decipher(message, steps):
    """Generate possible decoded messages for different shifts.

    Args:
        message (str): Encrypted message.
        steps (int): Maximum number of shifts to try.

    Returns:
        list: Possible decoded messages with their shift values.
    """
    results = []

    # Try each possible shift from 1 to the specified limit.
    for i in range(1, steps + 1):
        deciphered = []

        for char in message:
            if char.isupper():
                codeNum = (((ord(char) - 65) - i) % 26) + 65
                deciphered.append(chr(codeNum))

            elif char.islower():
                codeNum = (((ord(char) - 97) - i) % 26) + 97
                deciphered.append(chr(codeNum))

            else:
                # Preserve the original non-alphabetic handling.
                deciphered.append(chr(256 - ord(char)))

        # Store each candidate message alongside its shift.
        results.append({
            "shift": i,
            "message": "".join(deciphered)
        })

    return results


def gridWalker(path):
    """Track movement through a two-dimensional grid.

    Args:
        path (str): Sequence of U, D, L and R movement commands.

    Returns:
        dict: Final position, Manhattan distance, number of unique
              positions and furthest distance from the origin.
    """
    x0, y0 = (0, 0)

    # Store the starting position.
    coordinates = {(x0, y0)}

    # Define the coordinate changes for each direction.
    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    distanceTracker = 0

    for move in path:
        if move in directions:
            # Apply the movement to the current coordinates.
            x1, y1 = directions[move]
            x0 += x1
            y0 += y1

            # Record every position visited.
            coordinates.add((x0, y0))

            # Calculate distance from the starting point.
            dist = int(abs(x0)) + int(abs(y0))

            # Update the furthest distance reached.
            if dist > distanceTracker:
                distanceTracker = dist

    finpos = (x0, y0)

    # Calculate the final Manhattan distance.
    manhattan_distance = abs(finpos[0]) + abs(finpos[1])

    # Count distinct positions visited.
    uniquePosition = len(set(coordinates))

    return {
        "final_position": finpos,
        "manhattan_distance": manhattan_distance,
        "unique_positions": uniquePosition,
        "furthest_distance_travelled": distanceTracker,
    }


def isBalanced(text):
    """Check whether brackets in a string are correctly balanced.

    Args:
        text (str): Input string containing brackets.

    Returns:
        bool: True if all brackets are balanced; otherwise False.
    """
    stack = []

    # Map each closing bracket to its matching opening bracket.
    Brackets = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    for char in text:
        if char in Brackets.values():
            # Push opening brackets onto the stack.
            stack.append(char)

        elif char in Brackets.keys():
            # Reject unmatched or incorrectly ordered brackets.
            if not stack or stack[-1] != Brackets[char]:
                return False

            # Remove the matching opening bracket.
            stack.pop()

    # An empty stack means all brackets were matched.
    return len(stack) == 0


def scoreword(word):
    """Calculate a score based on word length and repeated letters.

    Args:
        word (str): Word to evaluate.

    Returns:
        int: Calculated word score.
    """
    # Remove non-alphabetic characters and convert to lowercase.
    word = "".join(
        [char for char in word if char.isalpha()]
    ).lower()

    if len(word) < 1:
        points = 0

    elif len(set(word)) < len(word):
        # Repeated letters result in half the word length.
        points = len(word) // 2

    else:
        # Words without repeated letters receive their full length.
        points = len(word)

    return points


def sortAscending(text):
    """Arrange characters in ascending Unicode order.

    Args:
        text (str): Input string.

    Returns:
        str: Characters arranged in ascending Unicode order.
    """
    characters = [i for i in text]
    arranged = []
    uniChar = []
    newString = []

    # Convert each character into its Unicode number.
    for char in characters:
        asciiNum = ord(char)
        uniChar.append(asciiNum)

    # Insert each Unicode number into its correct position.
    for num in uniChar:
        if not arranged:
            arranged.append(num)

        else:
            inserted = False

            for charPos in range(len(arranged)):
                # Use less-than to maintain ascending order.
                if num < arranged[charPos]:
                    arranged.insert(charPos, num)
                    inserted = True
                    break

            if not inserted:
                arranged.append(num)

    # Convert the sorted Unicode numbers back into characters.
    for num in arranged:
        new = chr(num)
        newString.append(new)

    newString = ''.join(newString)

    return newString


def daysToDeadline(submission_day):
    """Calculate the time remaining until a specified deadline.

    Args:
        submission_day (str): Date in dd/mm/yyyy or day Month year format.

    Returns:
        dict: Deadline status and remaining time, or an error message.
    """
    from datetime import datetime, date

    try:
        # Remove unnecessary spaces from the supplied date.
        submission_day = submission_day.strip()

        # First try the numeric date format.
        try:
            deadline = datetime.strptime(
                submission_day, '%d/%m/%Y'
            ).date()

        except ValueError:
            # If that fails, try a date containing the month name.
            deadline = datetime.strptime(
                submission_day.title(), '%d %B %Y'
            ).date()

        # Calculate the difference between today and the deadline.
        currentDate = date.today()
        numdays = deadline - currentDate

        # Identify deadlines that have already passed.
        if numdays.days < 0:
            return {
                "status": "passed",
                "days_remaining": numdays.days
            }

        # Convert remaining days into weeks and additional days.
        weekslft = numdays.days // 7
        dayslft = numdays.days % 7

    except (ValueError, AttributeError):
        # Return a helpful message when the date is invalid.
        return {
            "error": 'Invalid input. Date format should be dd/mm/yyyy or "day Month year".'
        }

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

