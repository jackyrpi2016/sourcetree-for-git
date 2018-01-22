# count character (giant essay)
# input a string, count how many times a character has appeared in this string

# use '''  ''' to input giant essay
message = ''' Romeo and Juliet is a tragedy written by William Shakespeare early in his career about two young star-crossed lovers whose deaths ultimately reconcile their feuding families. It was among Shakespeare's most popular plays during his lifetime and along with Hamlet, is one of his most frequently performed plays. Today, the title characters are regarded as archetypal young lovers.

Romeo and Juliet belongs to a tradition of tragic romances stretching back to antiquity. The plot is based on an Italian tale translated into verse as The Tragical History of Romeus and Juliet by Arthur Brooke in 1562 and retold in prose in Palace of Pleasure by William Painter in 1567. Shakespeare borrowed heavily from both but expanded the plot by developing a number of supporting characters, particularly Mercutio and Paris. Believed to have been written between 1591 and 1595, the play was first published in a quarto version in 1597. The text of the first quarto version was of poor quality, however, and later editions corrected the text to conform more closely with Shakespeare's original.

Shakespeare's use of his poetic dramatic structure (especially effects such as switching between comedy and tragedy to heighten tension, his expansion of minor characters, and his use of sub-plots to embellish the story) has been praised as an early sign of his dramatic skill. The play ascribes different poetic forms to different characters, sometimes changing the form as the character develops. Romeo, for example, grows more adept at the'''


count = {}  # use dictionary, 'character': count times

for character in message.upper():
    count.setdefault(character, 0)  # if character not exists, create character as the key, and value as 0
    count[character] = count[character] + 1  # increase the count by 1
    
print(count)
