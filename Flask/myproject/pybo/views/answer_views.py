# 답변 블루프린트 만들기

from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

# question_detail.html에서 정의한 form의 method가 post였으므로 여기서도 동일하게 맞춰줘야함
@bp.route('/create/<int:question_id>', methods=('POST',))

# question_id는 url에서 전달됨
def create(question_id):
    question = Question.query.get_or_404(question_id)

    # request.form['content'] == post 폼 방식으로 전송된 데이터 항목 중 name 속성이 content인 값
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now())

    # question.answer_set은 질문에 달린 답변들을 의미.
    # question과 answer 모델이 연결되어 있어 backref에 설정한 answer_set 사용 가능
    question.answer_set.append(answer)
    db.session.commit()
    
    # 답변 생성 후 화면 이동하도록 redirect 함수 사용함
    return redirect(url_for('question.detail', question_id=question_id))