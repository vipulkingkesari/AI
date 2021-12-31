
start :-
  ansi_format([bold,fg(green)], 'Career Advisory System. ~w', ['']),nl,
  ansi_format([bold], 'Welcome !! We will try to advice best career option for you. ~w', ['']),nl,
  write('We will give you different options.'), nl,
  reset_values,
  readFromFile,
  advice_career(Option).


readFromFile:-
  setup_call_cleanup(
    open('E:/sem 7/AI/AI_A5_Vipul_2018118/facts.txt',read,Input),
    (
      repeat,
      read_term(Input, X, []),
      read_from_file(X),asserta(X), !
    ),
    close(Input)
  ).


advice_career(Option) :-career(Option), !.

:- dynamic(result/2).


reset_values :-retract(result(_, _)),fail.
reset_values.



career(ms) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(tech),
  given_exam(gre),
  write('You look  to be interested in research.'),nl,
  write('So, you can go for higher studies'),nl,
  ansi_format([bold,fg(magenta)], ' Suggestion: Masters in Science ~w', ['']).


career(mtech) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(tech),
  given_exam(gate),
  write(' '),
  write('You seems to be interested in research.'),nl,
  write('You have cleared gate cutoff and you are interested in technology.'),nl,
  write('So, you can go for higher studies'),nl,
  ansi_format([bold,fg(magenta)], ' Suggestion: Masters in Technology. ~w', ['']).


career(mba) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(tech), 
  given_exam(cat),
  write('You seems to be interested in business.'),nl,
  write('You have cleared CAT cutoff and you have good management skills.'),nl,
  write('You can go for higher studies'),nl,
  ansi_format([bold,fg(magenta)], ' Suggestion: Masters in Business Administration. ~w', ['']).

  career(job) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(tech), 
  given_exam(none),
  coding(yes),
  write('You seems to be interested in coding .'),nl,
  write('So, you can go for an IT Job'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 1. Software developer. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Data Anayst. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Technical researcher. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 4. Cyber Security Analyst. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 5. System Designer. ~w', ['']).

  career(others) :-
  physical_or_mental(mental),
  aptitute(no),
  tech_or_nontech(tech),  
   business_oriented(no),
  traveller_nontraveller(traveller),
  creative_and_innovative(yes),
  write('You look like a creative and innovative person with technical knowledge.'),nl,
  write('You  like to travel a lot. '),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 1. Event Planner. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Journalism. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Blogger. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 4. Photographer if you are interested in photography.. ~w', ['']).


  career(others) :-
  physical_or_mental(mental),
  aptitute(no),
  tech_or_nontech(nontech),  
  traveller_nontraveller(nontraveller),
  creative_and_innovative(yes),
  write('You seems like a creative and innovative person.'),nl,
  write('But you do not like travelling and wants to do something by staying at a place only'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 2. Interior Designer. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Artist. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Fashion Designer.. ~w', ['']).


career(job) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(tech),
  given_exam(none),
  coding(no),
  write('You do not like coding.'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 1. Public Sector. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Teaching profile. ~w', ['']).

career(army) :-
  physical_or_mental(physical),
  aptitute(yes),
  leadership(yes),
  risk_taker(yes),
  write('You look like  to be physically fit.'),nl,
  write('You are a risk taker and can adapt to any situation.'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 1. Join India Army Force. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Join India Air Force. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Join India Navy Force. ~w', ['']).

career(business) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(nontech),   
  business_oriented(yes),
  write('You are a non-technological person but you are good in aptitute and you are a risk taker.'),nl,
  write('You are interested in business and you have good management skills and well as you are a good leadership.'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 1. You can start your own business. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Be an entrepreneaur. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Join any business related company. ~w', ['']).





career(others) :-
  physical_or_mental(mental),
  aptitute(yes),
  tech_or_nontech(nontech),  
  business_oriented(no),
  traveller_nontraveller(nontraveller),
  creative_and_innovative(yes),
  write('You seems like a creative and innovative person.'),nl,
  write('But you do not like travelling and wants to do something by staying at a place only'),nl,
  write('We would suggest you following job options'),nl,
  ansi_format([bold,fg(magenta)], ' 2. Interior Designer. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 2. Artist. ~w', ['']),nl,
  ansi_format([bold,fg(magenta)], ' 3. Fashion Designer.. ~w', ['']).







career(others):-
ansi_format([bold,fg(green)], 'Sorry, we are not able to predict you the career in future. we were not able to get your all details. ~w', ['']),nl,
write('You can take try a hand on new techs and explore your self.').

read_from_file(end_of_file):- !.
read_from_file(X):-
  asserta(X),!,
  fail.