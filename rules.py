class Rule:
    '''所有规则的基类'''
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)

class HeadingRule(Rule):
    type = 'heading'
    def condition(self,block):
        return not '\n' in block and len(block)<=70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'titile'
    first = True

    def condition(self,block):
        if not self.first:return False
        self.first = False
        return HeadingRule.condition(sel,block)

class ListItemRule(Rule):
    type = 'listitem'

    def condition(self,block):
        return block[0] == '-'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:])
        handler.end(self.type)
