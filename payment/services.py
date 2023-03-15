from payment.models import Payment


def get_course(pk):
    course = Payment.objects.filter(user=pk)
    ss = course.last()
    # for i in course:
    #     ss.append(i)
    return ss