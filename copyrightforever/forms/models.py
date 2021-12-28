from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class VirtualArtWorkForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_form = models.BooleanField(default=True, help_text='Change this to false when work done of this form')
    paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=19,default='VA VitualArts Work', null=True, blank=True)

    # form_start_from here
    name = models.CharField(max_length=120, default='', null=True, blank=True)
    email_address = models.EmailField(default='', null=True, blank=True)
    mailing_address = models.TextField(default='', null=True, blank=True)
    city = models.CharField(max_length=60, default='', null=True, blank=True)
    state = models.CharField(max_length=20, default='', null=True, blank=True)
    zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    # section_1
    title_of_work = models.CharField(max_length=256, default='', null=True, blank=True)
    prior_title = models.CharField(max_length=256, default='', null=True, blank=True)
    title_of_collective_work = models.CharField(max_length=256, default='', null=True, blank=True)
    volume = models.CharField(max_length=120, default='', null=True, blank=True)
    number = models.CharField(max_length=120, default='', null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    pages = models.CharField(max_length=5, default='', null=True, blank=True)

    # section_2
    name_of_author = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire = models.BooleanField(default=False)
    citizen_of = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous = models.BooleanField(default=False)
    authorship_pseudonymous = models.BooleanField(default=False)
    dimensional_sculpture = models.BooleanField(default=False)
    dimensional_artwork = models.BooleanField(default=False)
    reproduction_of_artwork = models.BooleanField(default=False)
    map = models.BooleanField(default=False)
    photograph = models.BooleanField(default=False)
    jewelery_design = models.BooleanField(default=False)
    technical_drawing = models.BooleanField(default=False)
    text = models.BooleanField(default=False)

    # section_3
    year_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)
    day = models.CharField(max_length=2, default='', null=True, blank=True)
    month = models.CharField(max_length=2, default='', null=True, blank=True)
    year = models.CharField(max_length=4, default='', null=True, blank=True)
    nation = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_4
    claimant_name = models.CharField(max_length=120, default='', null=True, blank=True)
    claimant_address = models.CharField(max_length=150, default='', null=True, blank=True)
    claimant_address_1 = models.CharField(max_length=150, default='', null=True, blank=True)
    reciepient_name = models.CharField(max_length=120, default='', null=True, blank=True)
    how_obtained_ownership = models.CharField(max_length=256, default='',
                                              help_text="like: gift, purchase or work for hire", null=True, blank=True)

    # section_5
    previously_registered = models.BooleanField(default=False)
    first_published_edition_of_work = models.BooleanField(default=False)
    first_application_by_the_author = models.BooleanField(default=False)
    changed_version_of_the_work = models.BooleanField(default=False)
    prior_reg_number = models.CharField(max_length=40, default='', null=True, blank=True)
    prior_reg_year = models.CharField(max_length=6, default='', null=True, blank=True)

    # section_6
    identify_preexisting_work = models.CharField(max_length=1056, default='', null=True, blank=True)
    describe_preexisting_work = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_7
    file = models.FileField(upload_to='files', )

    # section_8
    employer_name = models.CharField(max_length=120, default='', null=True, blank=True)
    employer_date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    date_of_hiring = models.DateField(auto_now_add=False, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    date_of_employing_copyright = models.DateField(auto_now_add=False, null=True, blank=True)
    sign_image = models.ImageField(upload_to="images", null=True, blank=True)

    # section_9
    certification_name = models.CharField(max_length=120, default='', null=True, blank=True)

    # -----------------------------------------------------------------------------------

    # from here continuation sheet start
    continuation_title = models.CharField(max_length=256, default='', null=True, blank=True)
    name_and_address = models.TextField(null=True, blank=True)

    # continuation_section_1
    name_of_author_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_1 = models.BooleanField(default=False)
    citizen_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_1 = models.BooleanField(default=False,)
    authorship_pseudonymous_1 = models.BooleanField(default=False)
    nature_of_authorship_1 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_2
    name_of_author_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_2 = models.BooleanField(default=False)
    citizen_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_2 = models.BooleanField(default=False)
    authorship_pseudonymous_2 = models.BooleanField(default=False)
    nature_of_authorship_2 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_3
    name_of_author_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_3 = models.BooleanField(default=False)
    citizen_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_3 = models.BooleanField(default=False)
    authorship_pseudonymous_3 = models.BooleanField(default=False)
    nature_of_authorship_3 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_form_last_fields_after_Authors
    continuation_name = models.CharField(max_length=120, default='', null=True, blank=True)
    continuation_date = models.CharField(max_length=10, default='', null=True, blank=True)
    continuation_address = models.TextField(default='', null=True, blank=True)
    continuation_city = models.CharField(max_length=60, default='', null=True, blank=True)
    continuation_state = models.CharField(max_length=20, default='', null=True, blank=True)
    continuation_zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'VA Form List'

    def __str__(self):
        return "VitualArts Work Form by: "+str(self.name)


class LiteraryWorkForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_form = models.BooleanField(default=True, help_text='Change this to false when work done of this form')
    paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=19,default='TX Literary Works', null=True, blank=True)

    # form_start_from here
    name = models.CharField(max_length=120, default='', null=True, blank=True)
    email_address = models.EmailField(default='', null=True, blank=True)
    mailing_address = models.TextField(default='', null=True, blank=True)
    city = models.CharField(max_length=60, default='', null=True, blank=True)
    state = models.CharField(max_length=20, default='', null=True, blank=True)
    zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    # section_1
    title_of_work = models.CharField(max_length=256, default='', null=True, blank=True)
    prior_title = models.CharField(max_length=256, default='', null=True, blank=True)
    title_of_collective_work = models.CharField(max_length=256, default='', null=True, blank=True)
    volume = models.CharField(max_length=120, default='', null=True, blank=True)
    number = models.CharField(max_length=120, default='', null=True, blank=True)
    issue_date = models.DateField(max_length=10, default='', null=True, blank=True)
    pages = models.CharField(max_length=5, default='', null=True, blank=True)

    # section_2
    name_of_author = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire = models.BooleanField(default=False)
    citizen_of = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous = models.BooleanField(default=False)
    authorship_pseudonymous = models.BooleanField(default=False)
    nature_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_3
    year_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)
    day = models.CharField(max_length=2, default='', null=True, blank=True)
    month = models.CharField(max_length=2, default='', null=True, blank=True)
    year = models.CharField(max_length=4, default='', null=True, blank=True)
    nation = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_4
    claimant_name = models.CharField(max_length=120, default='', null=True, blank=True)
    claimant_address = models.CharField(max_length=150, default='', null=True, blank=True)
    claimant_address_1 = models.CharField(max_length=150, default='', null=True, blank=True)
    reciepient_name = models.CharField(max_length=120, default='', null=True, blank=True)
    how_obtained_ownership = models.CharField(max_length=256, default='',
                                              help_text="like: gift, purchase or work for hire", null=True, blank=True)

    # section_5
    previously_registered = models.BooleanField(default=False)
    first_published_edition_of_work = models.BooleanField(default=False)
    first_application_by_the_author = models.BooleanField(default=False)
    changed_version_of_the_work = models.BooleanField(default=False)
    prior_reg_number = models.CharField(max_length=40, default='', null=True, blank=True)
    prior_reg_year = models.CharField(max_length=6, default='', null=True, blank=True)

    # section_6
    identify_preexisting_work = models.CharField(max_length=1056, default='', null=True, blank=True)
    describe_preexisting_work = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_7
    file = models.FileField(upload_to='files', )

    # section_8
    employer_name = models.CharField(max_length=120, default='', null=True, blank=True)
    employer_date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    date_of_hiring = models.DateField(auto_now_add=False, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    date_of_employing_copyright = models.DateField(auto_now_add=False, null=True, blank=True)
    sign_image = models.ImageField(upload_to="images", null=True, blank=True)

    # section_9
    certification_name = models.CharField(max_length=120, default='', null=True, blank=True)

    # -----------------------------------------------------------------------------------

    # from here continuation sheet start
    continuation_title = models.CharField(max_length=256, default='', null=True, blank=True)
    name_and_address = models.TextField(null=True, blank=True)

    # continuation_section_1
    name_of_author_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_1 = models.BooleanField(default=False)
    citizen_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_1 = models.BooleanField(default=False,)
    authorship_pseudonymous_1 = models.BooleanField(default=False)
    nature_of_authorship_1 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_2
    name_of_author_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_2 = models.BooleanField(default=False)
    citizen_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_2 = models.BooleanField(default=False)
    authorship_pseudonymous_2 = models.BooleanField(default=False)
    nature_of_authorship_2 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_3
    name_of_author_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_3 = models.BooleanField(default=False)
    citizen_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_3 = models.BooleanField(default=False)
    authorship_pseudonymous_3 = models.BooleanField(default=False)
    nature_of_authorship_3 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_form_last_fields_after_Authors
    continuation_name = models.CharField(max_length=120, default='', null=True, blank=True)
    continuation_date = models.CharField(max_length=10, default='', null=True, blank=True)
    continuation_address = models.TextField(default='', null=True, blank=True)
    continuation_city = models.CharField(max_length=60, default='', null=True, blank=True)
    continuation_state = models.CharField(max_length=20, default='', null=True, blank=True)
    continuation_zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'TX Form List'

    def __str__(self):
        return "Literary Works Form by: "+str(self.name)


class SoundRecordingForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_form = models.BooleanField(default=True, help_text='Change this to false when work done of this form')
    paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=19,default='SR Sound Recording', null=True, blank=True)

    # form_start_from here
    name = models.CharField(max_length=120, default='', null=True, blank=True)
    email_address = models.EmailField(default='', null=True, blank=True)

    # section_1
    title_of_work = models.CharField(max_length=256, default='', null=True, blank=True)
    prior_title = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_2
    name_of_author = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire = models.BooleanField(default=False)
    citizen_of = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous = models.BooleanField(default=False)
    authorship_pseudonymous = models.BooleanField(default=False)
    nature_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_3
    year_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)
    day = models.CharField(max_length=3, default='', null=True, blank=True)
    month = models.CharField(max_length=3, default='', null=True, blank=True)
    year = models.CharField(max_length=5, default='', null=True, blank=True)
    nation = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_4
    claimant_name = models.CharField(max_length=120, default='', null=True, blank=True)
    claimant_address = models.CharField(max_length=150, default='', null=True, blank=True)
    claimant_address_1 = models.CharField(max_length=150, default='', null=True, blank=True)
    reciepient_name = models.CharField(max_length=120, default='', null=True, blank=True)
    how_obtained_ownership = models.CharField(max_length=256, default='',
                                              help_text="like: gift, purchase or work for hire", null=True, blank=True)

    # section_5
    previously_registered = models.BooleanField(default=False)
    first_published_edition_of_work = models.BooleanField(default=False)
    first_application_by_the_author = models.BooleanField(default=False)
    changed_version_of_the_work = models.BooleanField(default=False)
    prior_reg_number = models.CharField(max_length=40, default='', null=True, blank=True)
    prior_reg_year = models.CharField(max_length=6, default='', null=True, blank=True)

    # section_6
    identify_preexisting_work = models.CharField(max_length=1056, default='', null=True, blank=True)
    describe_preexisting_work = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_7
    file = models.FileField(upload_to='files', )

    # section_8
    employer_name = models.CharField(max_length=120, default='', null=True, blank=True)
    employer_date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    date_of_hiring = models.DateField(auto_now_add=False, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    date_of_employing_copyright = models.DateField(auto_now_add=False, null=True, blank=True)
    city = models.CharField(max_length=120, default='', null=True, blank=True)
    state = models.CharField(max_length=120, default='', null=True, blank=True)
    zipcode = models.CharField(max_length=120, default='', null=True, blank=True)
    sign_image = models.ImageField(upload_to="images", null=True, blank=True)

    # section_9
    certification_name = models.CharField(max_length=120, default='', null=True, blank=True)

    # -----------------------------------------------------------------------------------

    # from here continuation sheet start
    continuation_title = models.CharField(max_length=256, default='', null=True, blank=True)
    name_and_address = models.TextField(null=True, blank=True)

    # continuation_section_1
    name_of_author_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_1 = models.BooleanField(default=False)
    citizen_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_1 = models.BooleanField(default=False,)
    authorship_pseudonymous_1 = models.BooleanField(default=False)
    nature_of_authorship_1 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_2
    name_of_author_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_2 = models.BooleanField(default=False)
    citizen_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_2 = models.BooleanField(default=False)
    authorship_pseudonymous_2 = models.BooleanField(default=False)
    nature_of_authorship_2 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_3
    name_of_author_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_3 = models.BooleanField(default=False)
    citizen_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_3 = models.BooleanField(default=False)
    authorship_pseudonymous_3 = models.BooleanField(default=False)
    nature_of_authorship_3 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_form_last_fields_after_Authors
    continuation_name = models.CharField(max_length=120, default='', null=True, blank=True)
    continuation_date = models.CharField(max_length=10, default='', null=True, blank=True)
    continuation_address = models.TextField(default='', null=True, blank=True)
    continuation_city = models.CharField(max_length=60, default='', null=True, blank=True)
    continuation_state = models.CharField(max_length=20, default='', null=True, blank=True)
    continuation_zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'SR Form List'

    def __str__(self):
        return "Sound Recording Form by: "+str(self.name)


class SerialWorkForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_form = models.BooleanField(default=True, help_text='Change this to false when work done of this form')
    paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=19,default='SE Serial Works', null=True, blank=True)

    # form_start_from here
    name = models.CharField(max_length=120, default='', null=True, blank=True)
    email_address = models.EmailField(default='', null=True, blank=True)

    # section_1
    title_of_work = models.CharField(max_length=256, default='', null=True, blank=True)
    volume = models.CharField(max_length=120, default='', null=True, blank=True)
    number = models.CharField(max_length=120, default='', null=True, blank=True)
    date_on_copies = models.CharField(max_length=10, default='', null=True, blank=True)
    frequency = models.CharField(max_length=5, default='', null=True, blank=True)
    prior_title = models.CharField(max_length=256, default='', null=True, blank=True)


    # section_2
    name_of_author = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire = models.BooleanField(default=False)
    citizen_of = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous = models.BooleanField(default=False)
    authorship_pseudonymous = models.BooleanField(default=False)
    nature_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_3
    year_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)
    day = models.CharField(max_length=3, default='', null=True, blank=True)
    month = models.CharField(max_length=3, default='', null=True, blank=True)
    year = models.CharField(max_length=5, default='', null=True, blank=True)
    nation = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_4
    claimant_name = models.CharField(max_length=120, default='', null=True, blank=True)
    claimant_address = models.CharField(max_length=150, default='', null=True, blank=True)
    claimant_address_1 = models.CharField(max_length=150, default='', null=True, blank=True)
    reciepient_name = models.CharField(max_length=120, default='', null=True, blank=True)
    how_obtained_ownership = models.CharField(max_length=256, default='',
                                              help_text="like: gift, purchase or work for hire", null=True, blank=True)

    # section_5
    previously_registered = models.BooleanField(default=False)
    first_published_edition_of_work = models.BooleanField(default=False)
    first_application_by_the_author = models.BooleanField(default=False)
    changed_version_of_the_work = models.BooleanField(default=False)
    prior_reg_number = models.CharField(max_length=40, default='', null=True, blank=True)
    prior_reg_year = models.CharField(max_length=6, default='', null=True, blank=True)

    # section_6
    identify_preexisting_work = models.CharField(max_length=1056, default='', null=True, blank=True)
    describe_preexisting_work = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_7
    file = models.FileField(upload_to='files', )

    # section_8
    employer_name = models.CharField(max_length=120, default='', null=True, blank=True)
    employer_date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    date_of_hiring = models.DateField(auto_now_add=False, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    date_of_employing_copyright = models.DateField(auto_now_add=False, null=True, blank=True)
    city = models.CharField(max_length=120, default='', null=True, blank=True)
    state = models.CharField(max_length=120, default='', null=True, blank=True)
    zipcode = models.CharField(max_length=120, default='', null=True, blank=True)
    sign_image = models.ImageField(upload_to="images", null=True, blank=True)

    # section_9
    certification_name = models.CharField(max_length=120, default='', null=True, blank=True)

    # -----------------------------------------------------------------------------------

    # from here continuation sheet start
    continuation_title = models.CharField(max_length=256, default='', null=True, blank=True)
    name_and_address = models.TextField(null=True, blank=True)

    # continuation_section_1
    name_of_author_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_1 = models.BooleanField(default=False)
    citizen_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_1 = models.BooleanField(default=False,)
    authorship_pseudonymous_1 = models.BooleanField(default=False)
    nature_of_authorship_1 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_2
    name_of_author_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_2 = models.BooleanField(default=False)
    citizen_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_2 = models.BooleanField(default=False)
    authorship_pseudonymous_2 = models.BooleanField(default=False)
    nature_of_authorship_2 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_3
    name_of_author_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_3 = models.BooleanField(default=False)
    citizen_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_3 = models.BooleanField(default=False)
    authorship_pseudonymous_3 = models.BooleanField(default=False)
    nature_of_authorship_3 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_form_last_fields_after_Authors
    continuation_name = models.CharField(max_length=120, default='', null=True, blank=True)
    continuation_date = models.CharField(max_length=10, default='', null=True, blank=True)
    continuation_address = models.TextField(default='', null=True, blank=True)
    continuation_city = models.CharField(max_length=60, default='', null=True, blank=True)
    continuation_state = models.CharField(max_length=20, default='', null=True, blank=True)
    continuation_zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'SE Form List'
    def __str__(self):
        return "Serial Works Form by: "+str(self.name)


class PerformingArtForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_form = models.BooleanField(default=True, help_text='Change this to false when work done of this form')
    paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=19,default='PA Performing Arts', null=True, blank=True)

    # form_start_from here
    name = models.CharField(max_length=120, default='', null=True, blank=True)
    email_address = models.EmailField(default='', null=True, blank=True)

    # section_1
    title_of_work = models.CharField(max_length=256, default='', null=True, blank=True)
    prior_title = models.CharField(max_length=256, default='', null=True, blank=True)
    nature_of_work = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_2
    name_of_author = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire = models.BooleanField(default=False)
    citizen_of = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous = models.BooleanField(default=False)
    authorship_pseudonymous = models.BooleanField(default=False)
    nature_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_3
    year_of_authorship = models.CharField(max_length=120, default='', null=True, blank=True)
    day = models.CharField(max_length=2, default='', null=True, blank=True)
    month = models.CharField(max_length=2, default='', null=True, blank=True)
    year = models.CharField(max_length=4, default='', null=True, blank=True)
    nation = models.CharField(max_length=120, default='', null=True, blank=True)

    # section_4
    claimant_name = models.CharField(max_length=120, default='', null=True, blank=True)
    claimant_address = models.CharField(max_length=150, default='', null=True, blank=True)
    claimant_address_1 = models.CharField(max_length=150, default='', null=True, blank=True)
    reciepient_name = models.CharField(max_length=120, default='', null=True, blank=True)
    how_obtained_ownership = models.CharField(max_length=256, default='',
                                              help_text="like: gift, purchase or work for hire", null=True, blank=True)

    # section_5
    previously_registered = models.BooleanField(default=False)
    first_published_edition_of_work = models.BooleanField(default=False)
    first_application_by_the_author = models.BooleanField(default=False)
    changed_version_of_the_work = models.BooleanField(default=False)
    prior_reg_number = models.CharField(max_length=40, default='', null=True, blank=True)
    prior_reg_year = models.CharField(max_length=6, default='', null=True, blank=True)

    # section_6
    identify_preexisting_work = models.CharField(max_length=1056, default='', null=True, blank=True)
    describe_preexisting_work = models.CharField(max_length=256, default='', null=True, blank=True)

    # section_7
    file = models.FileField(upload_to='files', )

    # section_8
    employer_name = models.CharField(max_length=120, default='', null=True, blank=True)
    employer_date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    date_of_hiring = models.DateField(auto_now_add=False, null=True, blank=True)
    employer_address = models.TextField(null=True, blank=True)
    date_of_employing_copyright = models.DateField(auto_now_add=False, null=True, blank=True)
    city = models.CharField(max_length=120, default='', null=True, blank=True)
    state = models.CharField(max_length=120, default='', null=True, blank=True)
    zipcode = models.CharField(max_length=120, default='', null=True, blank=True)
    sign_image = models.ImageField(upload_to="images", null=True, blank=True)


    # section_9
    certification_name = models.CharField(max_length=120, default='', null=True, blank=True)

    # -----------------------------------------------------------------------------------

    # from here continuation sheet start
    continuation_title = models.CharField(max_length=256, default='', null=True, blank=True)
    name_and_address = models.TextField(null=True, blank=True)

    # continuation_section_1
    name_of_author_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_1 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_1 = models.BooleanField(default=False)
    citizen_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_1 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_1 = models.BooleanField(default=False,)
    authorship_pseudonymous_1 = models.BooleanField(default=False)
    nature_of_authorship_1 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_2
    name_of_author_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_2 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_2 = models.BooleanField(default=False)
    citizen_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_2 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_2 = models.BooleanField(default=False)
    authorship_pseudonymous_2 = models.BooleanField(default=False)
    nature_of_authorship_2 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_section_3
    name_of_author_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    year_of_birth_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    year_of_death_3 = models.CharField(max_length=4, default='', null=True, blank=True)
    work_for_hire_3 = models.BooleanField(default=False)
    citizen_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    domiciled_of_3 = models.CharField(max_length=120, default='', null=True, blank=True)
    authorship_anonymous_3 = models.BooleanField(default=False)
    authorship_pseudonymous_3 = models.BooleanField(default=False)
    nature_of_authorship_3 = models.CharField(max_length=120, default='', null=True, blank=True)

    # continuation_form_last_fields_after_Authors
    continuation_name = models.CharField(max_length=120, default='', null=True, blank=True)
    continuation_date = models.CharField(max_length=10, default='', null=True, blank=True)
    continuation_address = models.TextField(default='', null=True, blank=True)
    continuation_city = models.CharField(max_length=60, default='', null=True, blank=True)
    continuation_state = models.CharField(max_length=20, default='', null=True, blank=True)
    continuation_zipcode = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'PA Form List'

    def __str__(self):
        return "PerformingArt Form by: "+str(self.name)