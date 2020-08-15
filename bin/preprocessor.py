import re

class PreprocessText:
    '''
    
     Preprocess news articles fed from files
     
     '''
    
    def __init__(self):
        pass
    
    def convertToLower(self, text):
        '''
        Convert text to lowercase

        Parameters
        ----------
        text : string
            text from news article

        Returns
        -------
        loweredText : string
            lower case characters.

        '''
        loweredText = text.lower()
        return loweredText
    
    def removeSpecialChar(self, text):
        '''
        remove special characters from text

        Parameters
        ----------
        text : string
            text from news article

        Returns
        -------
        loweredText : string
            text without special characters
        '''
        processedText = re.sub(',|;|<|>|', '', text)
        return processedText
    
    
    
# if __name__ == "__main__":
#     proprocessObj = PreprocessText()
#     text =  "of that software about it, so they can make and release the proper adjustments."
#     loweredText = preprocessObj.convertToLower(text)
#     filteredText = preprocessObj.removeSpecialChar(loweredText)
#     print('filtered text: {}.'.format(filteredText))