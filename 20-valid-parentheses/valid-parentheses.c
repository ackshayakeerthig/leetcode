typedef struct st{
    char data;
    struct st * next;
}* STACK;

STACK getnode(){
    return (STACK)malloc(sizeof(struct st));
}

STACK push(STACK top, char ch){
    STACK newnode = getnode();
    newnode->data = ch;
    newnode->next = top;
    return newnode;
}

STACK pop(STACK top, char * temp){
    if (top == NULL){
        *temp='\0';
        return top;
    }
    *temp = top->data;
    STACK dummy = top;
    top = top->next;
    free(dummy);
    return top;
}

char opp(char ch){
    switch(ch){
        case ')': return '(';
        case ']': return '[';
        case '}': return '{';
        default: return '\0';
    }
}

bool isValid(char* s) {
    int i = 0;
    char x;
    STACK stack = NULL;
    while (s[i] != 0){
        switch(s[i]){
            case '(':
            case '{':
            case '[':
                stack = push(stack, s[i]);
                break;
            case ')':
            case '}':
            case ']':
                stack = pop(stack, &x);
                if (x != opp(s[i])){
                    return 0;
                }
                break;
        }
        i++;
    }
    if (stack != NULL){
        return 0;
    }
    return 1;
}
