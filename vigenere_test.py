import os
import importlib.util
import re
import time

blue = "\033[1;34m"
red = "\033[31m"
green = "\033[32m"
reverse = "\033[;7m"
white = "\033[0m"
reset =  "\033[0;0m"

def testAll(filePath):
  spec = importlib.util.spec_from_file_location(os.path.splitext(filePath)[0], filePath)
  vigenere = importlib.util.module_from_spec(spec)

  try:
    spec.loader.exec_module(vigenere)
  except Exception as error:
    print("An error occured while importing your file:")
    print(red + str(error) + reset)
    return

  # print("\033c")

  print(f"\n     {blue}____________________{white}\n     VIGENERE SOLVER TEST   \n     {blue}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{white}\n")

  # encrypt_vigenere()
  print(reverse + " 1) encrypt_vigenere() " + white)

  test(vigenere, "encrypt_vigenere", [
    [
      ["Bokito and Einstein have the same birthday!", "ape"],
      "Bdoiis ach Exrsiiic laki twi spqe qmrildpc!"
    ], [
      ["Time you enjoy wasting, wasn’t wasted", "johnlennon"],
      "Cwtr jsh rbwxm dndxvau, jjgu’g hefgsq"
    ], [
      ["Never regret anything that made you smile", "marktwain"],
      "Zemok neoeqt rxrphqas tykm ialr kol cfelm"
    ], [
      ["Lorem  ipsum  dolor  sit  amet", "z"],
      "Knqdl  hortl  cnknq  rhs  zlds"
    ], [
      ["Not all those who wander are lost", "jrrtolkien"],
      "Wfk tzw dpsfn nyh klxlie jiv ecdd"
    ], [
      ["@^#* $%!&", "symbols"],
      "@^#* $%!&"
    ], [
      ["", "empty"],
      ""
    ], [
      ["    !", "spaces"],
      "    !"
    ]
  ])

  # decrypt_vigenere()
  print(reverse + " 2) decrypt_vigenere() " + white)

  test(vigenere, "decrypt_vigenere", [
    [
      ["Bdoiis ach Exrsiiic laki twi spqe qmrildpc!", "ape"],
      "Bokito and Einstein have the same birthday!"
    ], [
      ["Cwtr jsh rbwxm dndxvau, jjgu’g hefgsq", "johnlennon"],
      "Time you enjoy wasting, wasn’t wasted"
    ], [
      ["Zemok neoeqt rxrphqas tykm ialr kol cfelm", "marktwain"],
      "Never regret anything that made you smile"
    ], [
      ["M abxock hnsp ge oycs rts akqc at n zpyzh.", "monkey"],
      "A monkey tail is also the name of a plant."
    ], [
      ["Wfk tzw dpsfn nyh klxlie jiv ecdd", "jrrtolkien"],
      "Not all those who wander are lost"
    ], [
      ["@^#* $%!&", "symbols"],
      "@^#* $%!&"
    ], [
      ["", "empty"],
      ""
    ], [
      ["    !", "spaces"],
      "    !"
    ]
  ])

  # quadgram_fitness()
  print(reverse + " 3) quadgram_fitness() " + white)

  test(vigenere, "quadgram_fitness", [
    [
      ["Wkh glh kdv ehhq fdvw!"],
      280.9567026
    ], [
      ["Lqdqlm ivl Kwvycmz!"],
      271.219286
    ], [
      ["The die has been cast!"],
      133.9146274206767
    ], [
      ["Divide and Conquer!"],
      124.09624865743508
    ], [
      ["@^#* $%!&"],
      0
    ], [
      ["Lorem  ipsum  dolor  sit  amet"],
      225.2347326563955
    ], [
      ["I came, I saw, I conquered"],
      174.96509864690154
    ], [
      ["qxakyx"],
      69
    ]
  ])

  # solve_vigenere()
  print(reverse + " 4) solve_vigenere() " + white)

  times = test(vigenere, "solve_vigenere", [
    [
      ["V id wueirl lk tb ml vvxk vn pweorndvkkdoaaeg wgirs.", 7],
      ("nirvana", "I am buried up to my neck in contradictionary flies.")
    ], [
      ["Bdoiis ach Exrsiiic laki twi spqe qmrildpc!", 3],
      ("ape", "Bokito and Einstein have the same birthday!")
    ], [
      ["L pjffhn wsxpn rsrms pvw oexhvgy wa xse wcnw hm gszk yc nooqq me", 10],
      ("lafontaine", "A person often meets his destiny on the road he took to avoid it")
    ], [
      ["Uksxslzhmf ski zeap. Pprq mvt xw bety sgh zeb pkc. Cwhtgi iia pnjwim. Wwdabvexw olmp lzrlxry xw sa gbmk jmmmez nvjlx", 10],
      ("steveirwin", "Crocodiles are easy. They try to kill and eat you. People are harder. Sometimes they pretend to be your friend first")
    ], [
      ["M abxock hnsp ge oycs rts akqc at n zpyzh.", 6],
      ("monkey", "A monkey tail is also the name of a plant.")
    ], [
      ["Ysvcyc fvn, cxh irpyxwt iqsf'er uhez. Xc'g irpyxwt iqsf'ir zhic hcfvat drv idx zvat", 10],
      ("johnnydepp", "People cry, not because they're weak. It's because they've been strong for too long")
    ], [
      ["Hzgrv wzp rrzq vwf czpdx hjcgvzqpv mb dkfv: kvp lw bgv gvpbtqk kzct pkc hdrh spd kdm zwlsj ks xabelru av", 10],
      ("oscarwilde", "There are only two great tragedies in life: one is not getting what you want and the other is getting it")
    ], [
      ["Rk'j mvp twf gqrk'l bpfmv fcrimso dpeg crbxg erm pbwxvlh ey nmarjy", 10],
      ("jrrtolkien", "It's the job that's never started that takes the longest to finish")
    ]
  ])

  # execution time
  print(reverse + " 5) execution time " + white)
  slow = [*filter(lambda e: e > 20, times)]
  if len(slow) > 0:
    print(red + "solve_vigenere is too slow")
    print("solve_vigenere must not take more than 20 seconds")
  else:
    print(green + "solve_vigenere always took less than 20 seconds")

  print(reset, end="")

def test(module, func, values):
  right = 0
  times = []
  printed = False

  if not hasattr(module, func):
    print(red + func + "does not exist")
    print()
    return
  f = getattr(module, func)
  for i, e in enumerate(values):
    if not printed:
      bar = "█" * i
      rest = "░" * (len(values)-i)
      print(f"Testing... {bar}{rest}", end="\r")
    inp = func + "(" + ", ".join(["\"" + ee + "\"" if ee * 0 == "" else str(ee) for ee in e[0]]) + ")"
    try:
      start = time.time()
      val = f(*e[0])
      end = time.time()
      if e[1] * 0 == 0:
        e[1] = round(e[1], 5)
        val = round(val, 5)
      if val == e[1]:
        right += 1
      else:
        print(white + inp)
        print("Expected output: " + green + str(e[1]).replace("\n", "\\n"))
        print(white + "Actual output:   " + red + str(val).replace("\n", "\\n"))
        print()
        printed = True
    except Exception as error:
      if not "end" in locals():
        end = time.time()
      print(white + inp)
      print("Expected output: " + green + str(e[1]).replace("\n", "\\n"))
      print(white + "Error:           " + red + str(error))
      print()
      printed = True
    times.append(end - start)
  if right == len(values):
    print(green, end="")
  print(f"{right}/{len(values)} test cases were correct")
  print()
  return times

err = "Unable to locate file, please try again"
stop = False
c = os.path.dirname(os.path.realpath(__file__))
settingsFile =  "test_settings.txt"

def askFile():
  while True:
    try:
      fileName = input("File name: ")
      if fileName == "" or fileName == "quit()" or fileName == "exit()":
        filePath = None
        break
      if not fileName.endswith(".py"):
        print("This file doesn't have the correct file extension, please try again")
        continue
      if os.path.isfile(os.path.join(c, fileName)):
        filePath = os.path.join(c, fileName)
        with open(os.path.join(c, settingsFile), "w") as f:
          f.write(filePath)
        break
      print(err)
    except: print(err)
  if filePath is not None:
    print()
    testAll(filePath)

if os.path.isfile(os.path.join(c, settingsFile)):
  with open(os.path.join(c, settingsFile), "r") as file:
      filePath = file.read()
  if os.path.isfile(filePath):
    testAll(filePath)
  else:
    print(err)
    askFile()
else:
  askFile()