from src.domain.di_container import summary_generator_llm

content = """
Welcome back to Week in Review. This week we’re looking at the internal chaos surrounding HP’s $116 million acquisition of AI Pin maker Humane; Mira Murati’s new AI venture coming out of stealth; Duolingo killing its iconic owl mascot with a Cybertruck; and more! Let’s get into it.

Humane’s AI pin is dead. The hardware startup announced that most of its assets have been acquired by HP for $116 million, less than half of the $240 million it raised in VC funding. The startup will immediately discontinue sales of its $499 AI Pins, and after February 28, the wearable will no longer connect to Humane’s servers. After that, the devices won’t be capable of calling, messaging, AI queries/responses, or cloud access. Customers who bought an AI Pin in the last 90 days are eligible for a refund, but anyone who bought a device before then is not.

Hours after the HP acquisition was announced, several Humane employees received job offers from HP with pay increases between 30% and 70%, plus HP stock and bonus plans, according to internal documents seen by TechCrunch and two sources who requested anonymity. Meanwhile, other Humane employees — especially those who worked closer to the AI Pin devices — were notified they were out of a job.

Apple’s long-awaited iPhone SE refresh has been revealed, three years after the last major update to the budget-minded smartphone. The 16e is part of an exclusive group of handsets capable of running Apple Intelligence due to the addition of an A18 processor. The iPhone 16e also ditched the Touch ID home button in favor of Face ID and swapped out the Lightning port in favor of USB-C. The iPhone 6e starts at $599 and will begin shipping February 28.
Uber vs. DoorDash: Uber is suing DoorDash, accusing its delivery rival of stifling competition by intimidating restaurant owners into exclusive deals. Uber alleges that DoorDash bullied restaurants into only working with them. Read more

Mira Murati’s next move: Former OpenAI CTO Mira Murati’s new AI startup, Thinking Machines Lab, has come out of stealth. The startup, which includes OpenAI co-founder John Schulman and former OpenAI chief research officer Barret Zoph, will focus on building collaborative “multimodal” systems. Read more

Introducing Grok 3: Elon Musk’s xAI released its latest flagship AI model, Grok 3, and unveiled new capabilities for the Grok iOS and web apps. Musk claims that the new family of models is a “maximally truth-seeking AI” that is sometimes “at odds with what is politically correct.” Read more

Hackers on Steam: Valve removed a video game from Steam that was essentially designed to spread malware. Security researchers found that whoever planted it modified an existing video game in an attempt to trick gamers into installing an info-stealer called Vidar. Read more

Another DEI U-turn: Mark Zuckerberg and Priscilla Chan’s charity will end internal DEI programs and stop providing “social advocacy funding” for racial equity and immigration reforms. The switch comes just weeks after the organization assured staff it would continue to support DEI efforts. Read more

Amazon shuts down its Android app store: Amazon will discontinue its app store for Android in August in an effort to put more focus on the company’s own devices. The company told developers that they will no longer be able to submit new apps to the store. Read more

Mark Zuckerberg’s rebrand didn’t pay off: A study by the Pew Research Center found that Americans’ views of Elon Musk and Mark Zuckerberg are more negative than positive. About 54% of U.S. adults say they have an unfavorable view of Musk while a whopping 67% feel negatively toward Zuckerberg. Read more

Noise-canceling headphones could hurt your brain: A new BBC report considers whether noise-canceling tech might be rewiring the brains of people who use it to tune out pesky background noise — and could lead to the brain forgetting how to filter sounds itself. Read more 
"""

summary = summary_generator_llm.generate_summary(content=content)
print(summary)
